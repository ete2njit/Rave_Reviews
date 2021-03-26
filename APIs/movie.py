#API CALLER TO PULL MOVIE DATA FROM TMDB
#Author: Madison Miatke

import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "../api-keys.env")
load_dotenv(dotenv_path)

#MOVIE CLASS
class Movie:
    def __init__(self,title,year,tmdbID,coverPhoto,description=None,directors=None,stars=None,length=None,genres=None):
        self.category="movie"
        self.title=title
        self.year=year
        self.tmdbID=tmdbID
        self.coverPhoto=coverPhoto
        self.directors=directors
        self.description=description
        self.stars=stars
        self.length=length
        self.genres=genres

    def __repr__(self):
        ret = ("Title: " + str(self.title) + "\n"
        + "Year: " + str(self.year) + "\n"
        + "TmdbID: " + str(self.tmdbID) + "\n"
        + "Cover Photo: " + str(self.coverPhoto) + "\n"
        + "Description: " + str(self.description) + "\n"
        + "Stars: " + str(self.stars) + "\n"
        + "Directors: " + str(self.directors) + "\n"
        + "Length: " + str(self.length) + "\n"
        + "Genres: " + str(self.genres) + "\n")
        return ret

#Use tmdbID to get the complete information for a movie
def getFullMovieInfoByID(tmdbID):
    url = "https://api.themoviedb.org/3/movie/"+str(tmdbID)+"?api_key="+os.environ['TMDB_API_KEY']
    response = requests.request("GET", url)
    responseDetails = response.json()

    if "success" in responseDetails.keys() and responseDetails['success'] == False:
        return None

    genreList = []
    if  "genres" in responseDetails.keys():
        for genres in responseDetails["genres"]:
            genreList.append(genres["name"])

    coverPhoto=None
    if "poster_path" in responseDetails.keys() and responseDetails["poster_path"]!=None:
        coverPhoto = "https://www.themoviedb.org/t/p/original" + responseDetails["poster_path"]

    year=None
    if "release_date" in responseDetails.keys() and len(responseDetails["release_date"]) > 4:
        year=responseDetails["release_date"][:4]

    url = "https://api.themoviedb.org/3/movie/"+str(tmdbID)+"/credits?api_key="+os.environ['TMDB_API_KEY']
    response = requests.request("GET", url)
    responseCredits = response.json()
    stars = []
    if "cast" in responseCredits.keys():
        for castMember in  responseCredits["cast"]:
            if castMember["popularity"] > 2.0:
                stars.append(castMember["name"])

    directors=[]
    if "crew" in responseCredits.keys():
        for crewMember in responseCredits["crew"]:
            if crewMember["job"]=="Director":
                directors.append(crewMember["name"])

    movie = Movie(
        responseDetails["title"],
        year,
        tmdbID,
        coverPhoto,
        responseDetails["overview"],
        directors,
        stars,
        responseDetails["runtime"],
        genreList
    )

    return movie

#Search for a movie using keywords in the title
def searchMovies(query, limit=10):
    page = 0
    count=0
    movies=[]
    while limit > count:
        page+=1
        url = "https://api.themoviedb.org/3/search/movie?query="+query.replace(" ","+")+"&api_key="+os.environ['TMDB_API_KEY']+"&page="+str(page)+"&include_adult=false"
        response = requests.request("GET", url)
        responseMovies = response.json()

        if "results" not in responseMovies.keys() or len(responseMovies["results"])==0:
            return movies

        for movie in responseMovies["results"]:
            if count >= limit:
                return movies

            coverPhoto=None
            if("poster_path" in movie.keys() and movie["poster_path"]!=None):
                coverPhoto = "https://www.themoviedb.org/t/p/original" + movie["poster_path"]

            year=None
            if "release_date" in movie.keys() and len(movie["release_date"]) > 4:
                year=movie["release_date"][:4]

            movies.append(Movie(movie["title"],year,str(movie["id"]),coverPhoto))
            count+=1
    return movies

#Movies currently in theaters
def getNowPlayingMovies(limit=10):
    movies = getMovies("now_playing", limit)
    return movies

#Movies trending (viewers growing)
def getTrendingMovies(limit=10):
    movies = getMovies("trending", limit)
    return movies

#Movies that are top rated
def getTopRatedMovies(limit=10):
    movies = getMovies("top_rated", limit)
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
    while limit > count:
        page+=1
        if typeOfLookUp=="trending":
            url = "https://api.themoviedb.org/3/trending/movie/week?page="+str(page)+"&api_key="+os.environ['TMDB_API_KEY']
        else:
            url = "https://api.themoviedb.org/3/movie/"+typeOfLookUp+"?page="+str(page)+"&api_key="+os.environ['TMDB_API_KEY']
        response = requests.request("GET", url)
        responseMovies = response.json()

        if "results" not in responseMovies.keys() or len(responseMovies["results"])==0:
            return movies

        for movie in responseMovies["results"]:
            if count >= limit:
                return movies

            coverPhoto=None
            if("poster_path" in movie.keys() and movie["poster_path"]!=None):
                coverPhoto = "https://www.themoviedb.org/t/p/original" + movie["poster_path"]

            year=None
            if "release_date" in movie.keys() and len(movie["release_date"]) > 4:
                year=movie["release_date"][:4]

            movies.append(Movie(movie["title"],year,str(movie["id"]),coverPhoto))
            count+=1
    return movies

"""
movies = getPopularMovies(3)
for movie in movies:
    print(movie)

movies = getUpcomingMovies(3)
for movie in movies:
    print(movie)

movies = getTopRatedMovies(2)
for movie in movies:
    print(movie)

movies = getTrendingMovies(37)
for movie in movies:
    print(movie)

movies = getNowPlayingMovies(32)
for movie in movies:
    print(movie)

movies = searchMovies("Rocket", 3)
for movie in movies:
    print(movie)

movie = movies[0]
print(getFullMovieInfoByID(movie.tmdbID))

print(getFullMovieInfoByID("tt0137523"))

movies = searchMovies("spongebob", 30)
for movie in movies:
    print(getFullMovieInfoByID(movie.tmdbID))
    
print(getFullMovieInfoByID("e4wrfddgf"))
"""
