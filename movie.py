#API CALLER TO PULL MOVIE DATA FROM IMDB AND TMDB
#Author: Madison Miatke

import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "api-keys.env")
load_dotenv(dotenv_path)

#MOVIE CLASS
class Movie:
    def __init__(self,title,year,imdbID,coverPhoto,description=None,directors=None,stars=None,length=None,rated=None,genres=None):
        self.catergory="movie"
        self.title=title
        self.year=year
        self.imdbID=imdbID
        self.coverPhoto=coverPhoto
        self.directors=directors
        self.description=description
        self.stars=stars
        self.length=length
        self.rated=rated
        self.genres=genres
    
    def toString(self):
        ret = ("Title: " + self.title + "\n"
        + "Year: " + str(self.year) + "\n"
        + "ImdbID: " + self.imdbID + "\n"
        + "Cover Photo: " + self.coverPhoto + "\n"
        + "Description: " + self.description + "\n"
        + "Stars: " + str(self.stars) + "\n"
        + "Directors: " + str(self.directors) + "\n"
        + "Length: " + str(self.length) + "\n"
        + "Rated: " + str(self.rated) + "\n"
        + "Genres: " + str(self.genres) + "\n")
        return ret

#Use imdbID to get the complete information for a movie
def getFullMovieInfoByID(imdbID):
    url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
    headers = {
        'x-rapidapi-key': os.environ['IMDB_API_KEY'],
        'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
    }   
    
    querystring = {"type":"get-movie-details","imdb":imdbID}
    response = requests.request("GET", url, headers=headers, params=querystring)
    responseDetails = response.json()
    
    
     
    movie = Movie(
        responseDetails["title"],
        responseDetails["year"],
        imdbID,
        getCoverPhoto(responseDetails["title"]),
        responseDetails["description"],
        responseDetails["directors"],
        responseDetails["stars"],
        responseDetails["runtime"],
        responseDetails["rated"],
        responseDetails["genres"]
    )
    
    return movie

#Use a movie title to get a poster photo
def getCoverPhoto(title):
    url = "https://api.themoviedb.org/3/search/movie?api_key="+ os.environ['TMDB_API_KEY']+ "&query=" + title.replace(" ","+") + ""   
    print(url)
    response = requests.request("GET", url)
    responseJSON = response.json()
    
    print(responseJSON)
    if responseJSON["total_results"] > 0:
        if(responseJSON["results"][0]["poster_path"]!=None):
            return ("https://www.themoviedb.org/t/p/original/" + responseJSON["results"][0]["poster_path"])
        else:
            return ""        
    else:
        return ""

#Search for a movie using keywords in the title
def searchMovies(query, limit=10):
    url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
    querystring = {"type":"get-movies-by-title","title":query}
    
    headers = {
        'x-rapidapi-key': os.environ['IMDB_API_KEY'],
        'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
    }   

    response = requests.request("GET", url, headers=headers, params=querystring)
    responseMovies = response.json()
    
    movies=[]
    count=0
    for movie in responseMovies["movie_results"]:
        if count == limit:
            return movies
        coverPhoto=getCoverPhoto(movie["title"])
        movies.append(Movie(movie["title"],movie["year"],movie["imdb_id"],coverPhoto))
        count+=1
        
        
    return movies

#Movies currently in theaters
def getNowPlayingMovies(limit=10):
    movies = getMovies("nowplaying", limit)
    return movies

#Movies recently added
def getRecentlyAddedMovies(limit=10):
    movies = getMovies("recently-added", limit)
    return movies    
    
#Movies that are trending (watchers growing)
def getTrendingMovies(limit=10):
    movies = getMovies("trending", limit)
    return movies    

#Movies that are being released soon
def getUpcomingMovies(limit=10):
    movies = getMovies("upcoming", limit)
    return movies   

#Movies that are being watched the most right now
def getPopularMovies(limit=10):
    movies = getMovies("popular", limit)
    return movies

#Used to run all the categorical calls above, if no type is given it will pick random movies
def getMovies(typeOfLookUp="random", limit=10):
    page = 0
    count=0
    movies=[]
    
    url = "https://movies-tvshows-data-imdb.p.rapidapi.com/"
    headers = {
        'x-rapidapi-key': os.environ['IMDB_API_KEY'],
        'x-rapidapi-host': "movies-tvshows-data-imdb.p.rapidapi.com"
    }    
    
    while limit > count:
        page+=1
        querystring = {"type":"get-"+typeOfLookUp+"-movies","page":page}
    
        response = requests.request("GET", url, headers=headers, params=querystring)
        responseMovies = response.json()
        
        for movie in responseMovies["movie_results"]:
            if count >= limit:
                return movies
            coverPhoto=getCoverPhoto(movie["title"])
            movies.append(Movie(movie["title"],movie["year"],movie["imdb_id"],coverPhoto))
            count+=1
        print(count)
    return movies

""" Test  runs  
movies = getPopularMovies(3)
for movie in movies:
    print(movie.toString())
    
movies = getUpcomingMovies(3)
for movie in movies:
    print(movie.toString())
        
movies = getTrendingMovies(3)
for movie in movies:
    print(movie.toString())
    
movies = getRecentlyAddedMovies(3)
for movie in movies:
    print(movie.toString())

movies = getNowPlayingMovies(3)
for movie in movies:
    print(movie.toString())

movies = searchMovies("spongebob", 3)
for movie in movies:
    print(movie.toString())
"""