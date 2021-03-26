#API CALLER TO PULL BOOK DATA FROM GOOGLE BOOK API AND NYT API
#Author: Madison Miatke

import requests
import json
import os
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv
import numpy as np

dotenv_path = join(dirname(__file__), "../api-keys.env")
load_dotenv(dotenv_path)

#BOOK CLASS
class Book:
    def __init__(self,isbn,title,cover,publishYear,publisher, description,authors,genres,pages,language):
        self.category="book"
        self.isbn=isbn
        self.title=title
        self.cover=cover
        self.publishYear=publishYear
        self.publisher=publisher
        self.description=description
        self.authors=authors
        self.genres=genres
        self.pages=pages
        self.language=language

    def __repr__(self):
        ret = ("ISBN: " + str(self.isbn) + "\n"
        + "Title: " + str(self.title) + "\n"
        + "Cover: " + str(self.cover) + "\n"
        + "Publish Year: " + str(self.publishYear) + "\n"
        + "Publisher: " + str(self.publisher) + "\n"
        + "Desciption: " + str(self.description) + "\n"
        + "Authors: " + str(self.authors) + "\n"
        + "Genres: " + str(self.genres) + "\n"
        + "Pages: " + str(self.pages) + "\n"
        + "Language: " + str(self.language) + "\n")
        return ret

#search for books from google book api given a query
def searchBooks(query, limit=10):
    books = []
    startIndex=0
    while limit>0:
        maxResults=40-(40-limit)
        if maxResults>40:
            maxResults=40
        url = ("https://www.googleapis.com/books/v1/volumes?q="+query
               +"&startIndex="+str(startIndex)
               +"&maxResults="+str(maxResults)
               +"&printType=books"
               +"&key="+os.environ['GOOGLE_BOOK_API_KEY'])
        response = requests.request("GET", url)
        books=np.append(books, parseBookData(response))
        limit-=maxResults
        startIndex+=(maxResults+1)
    return books

#search for books from google book api given a genre
def getBooksByGenre(genre, limit=10):
    books = []
    startIndex=0
    while limit>0:
        maxResults=40-(40-limit)
        if maxResults>40:
            maxResults=40
        url = "https://www.googleapis.com/books/v1/volumes?q=subject:"+genre+"&printType=books&key=" + os.environ['GOOGLE_BOOK_API_KEY']
        response = requests.request("GET", url)
        books=np.append(books, parseBookData(response))
        limit-=maxResults
        startIndex+=(maxResults+1)
    return books

#search for books from google book api given an author name
def getBooksByAuthor(author, limit=10):
    books = []
    startIndex=0
    while limit>0:
        maxResults=40-(40-limit)
        if maxResults>40:
            maxResults=40
        url = "https://www.googleapis.com/books/v1/volumes?q=inauthor:"+author+"&printType=books&key=" + os.environ['GOOGLE_BOOK_API_KEY']
        response = requests.request("GET", url)
        books=np.append(books, parseBookData(response))
        limit-=maxResults
        startIndex+=(maxResults+1)
    return books

#get a book object from google book api given a ISBN number
def getBookByISBN(isbn):
    url = "https://www.googleapis.com/books/v1/volumes?q=isbn:"+isbn+"&printType=books&key=" + os.environ['GOOGLE_BOOK_API_KEY']
    response = requests.request("GET", url)
    return parseBookData(response)

#parse book data into a list of book objects given a google api response
def parseBookData(response):
    responseDetails = response.json()
    books=[]
    fields=["industryIdentifiers","title","imageLinks","publishedDate","publisher","description","authors","categories","pageCount","language"]
    if "items" not in responseDetails.keys():
        return []
    for item in responseDetails["items"]:
        volume = item["volumeInfo"]

        #check to see if fields exist as keys, if they dont set them to None
        for field in fields:
            if field not in volume.keys():
                volume[field]=None

        book = Book(
            getISBN(volume["industryIdentifiers"]),
            volume["title"],
            getCover(volume["imageLinks"]),
            getPublishingYear(volume["publishedDate"]),
            volume["publisher"],
            volume["description"],
            volume["authors"],
            volume["categories"],
            volume["pageCount"],
            volume["language"]
        )

        books.append(book)

    return books

#gets best sellers given a best seller category
def getBestSellers(category='hardcover-fiction'):
    books=[]

    #use NYT api to get best sellers
    url = "https://api.nytimes.com/svc/books/v3/lists/current/"+category+".json?api-key=" + os.environ['NYT_API_KEY']
    response = requests.request("GET", url)
    jsonResponse = response.json()

    if "results" not in jsonResponse.keys():
        return books

    #use isbn from NYT response to search for the best sellers in the google api
    for book in jsonResponse["results"]["books"]:
        googleBook = getBookByISBN(book["primary_isbn13"])
        if googleBook == []:
            googleBook = getBookByISBN(book["primary_isbn10"])
        if  googleBook != []:
            books.append(googleBook[0])

    return books

#gets list of the useable best seller categories
def getBestSellerCategories():
    categories = []
    url = "https://api.nytimes.com/svc/books/v3/lists/names.json?api-key=" + os.environ['NYT_API_KEY']
    response = requests.request("GET", url)
    jsonResponse = response.json()

    if "results" not in jsonResponse.keys():
        return categories

    for cat in jsonResponse["results"]:
        categories.append(cat["list_name_encoded"])
    return categories

#used to parse ISBN, and catch if one is not available
def getISBN(identifiers):
    if identifiers == None:
        return None
    return identifiers[0]["identifier"]

#used to parse cover image, and catch if one is not available
def getCover(imageLinks):
    if imageLinks==None:
        return None
    return imageLinks["thumbnail"]

#used to parse publish year, and catch if one is not available
def getPublishingYear(publishDate):
    if publishDate==None:
        return None
    return publishDate[:4]

"""
books = searchBooks("Sunshine",23)
for book in books:
    print(book)
print("NUMBER:" + str(books.size))

books = getBooksByGenre("Juvenile Fiction")
for book in books:
    print(book)


books = getBookByISBN("0545317010")
for book in books:
    print(book)

books = getBooksByAuthor("Mark Twain")
for book in books:
    print(book)

books = getBooksByGenre("Horror")
for book in books:
    print(book)

print(getBestSellerCategories())

bestSellers = getBestSellers("hardcover-nonfiction")
for bestSeller in bestSellers:
    print(bestSeller)
"""
