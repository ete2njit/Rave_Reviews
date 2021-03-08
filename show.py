#API CALLER TO PULL TV SHOW DATA FROM TMDB
#Author: Madison Miatke

import requests
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), "api-keys.env")
load_dotenv(dotenv_path)

#SHOW CLASS
class Show:
    def __init__(self,title,release_date,tmdbID,coverPhoto,description=None,creators=None,episodeLength=None,stillAiring=None,genres=None,countries=None,networks=None):
        self.catergory="tvshow"
        self.title=title
        self.release_date=release_date
        self.tmdbID=tmdbID
        self.coverPhoto=coverPhoto
        self.creators=creators
        self.description=description
        self.episodeLength=episodeLength
        self.stillAiring=stillAiring
        self.genres=genres
        self.countries=countries
        self.networks=networks
    
    def toString(self):
        ret = ("Title: " + self.title + "\n"
        + "Release Date: " + str(self.release_date) + "\n"
        + "tmdbID: " + str(self.tmdbID) + "\n"
        + "Cover Photo: " + str(self.coverPhoto) + "\n"
        + "Creators: " + str(self.creators) + "\n"
        + "Description: " + self.description + "\n"
        + "Episode Length: " + str(self.episodeLength) + "\n"
        + "Still Airing: " + str(self.stillAiring) + "\n"
        + "Genres: " + str(self.genres) + "\n"
        + "Countries: " + str(self.countries) + "\n"
        + "Networks: " + str(self.networks) + "\n")
        return ret

#Use tmdbID to get the complete information for a show
def getFullShowInfoByID(tmdbID):
    url = "https://api.themoviedb.org/3/tv/"+str(tmdbID)+"?api_key="+os.environ['TMDB_API_KEY']
    response = requests.request("GET", url)
    responseJSON = response.json()
    
    creators = []
    for creator in responseJSON["created_by"]:
        creators.append(creator["name"])
    
    genres = []
    for genre in responseJSON["genres"]:
        genres.append(genre["name"])
    
    networks = []
    for network in responseJSON["networks"]:
        networks.append(network["name"])
     
    if responseJSON["poster_path"]==None:
        responseJSON["poster_path"]=""
    else:
        responseJSON["poster_path"]="https://www.themoviedb.org/t/p/original" + responseJSON["poster_path"]
     
    show = Show(
        responseJSON["name"],
        responseJSON["first_air_date"],
        tmdbID,
        responseJSON["poster_path"],
        responseJSON["overview"],
        creators,
        responseJSON["episode_run_time"][0],
        responseJSON["in_production"],
        genres,
        responseJSON["origin_country"],
        networks
    )
    
    return show

#Search for a shows using keywords in the title
def searchShows(query, limit=10):
    page = 0
    count=0
    shows=[]
    
    while limit > count:
        page+=1
        url = "https://api.themoviedb.org/3/search/tv?api_key="+os.environ['TMDB_API_KEY']+"&query="+query+"&page="+str(page)+"&include_adult=false"
        response = requests.request("GET", url)
        responseJSON = response.json()
        
        for show in responseJSON["results"]:
            if count >= limit:
                return shows
            if show["poster_path"]==None:
                show["poster_path"]=""
            else:
                show["poster_path"]="https://www.themoviedb.org/t/p/original" + show["poster_path"]
            shows.append(Show(show["name"],show["first_air_date"],show["id"],show["poster_path"]))
            count+=1
        print(count)
    return shows

#Get list of top rated shows
def getTopRatedShows(limit=10):
    movies = getShows("top_rated", limit)
    return movies  

#Get list of trending shows
def getTrendingShows(timeWindow="week", limit=10): #Time window can be "day" or "week"
    page = 0
    count=0
    shows=[]
    
    while limit > count:
        url = "https://api.themoviedb.org/3/trending/tv/week?api_key="+os.environ['TMDB_API_KEY']
        response = requests.request("GET", url)
        responseJSON = response.json()
        
        for show in responseJSON["results"]:
            if count >= limit:
                return shows
            if show["poster_path"]==None:
                show["poster_path"]=""
            else:
                show["poster_path"]="https://www.themoviedb.org/t/p/original" + show["poster_path"]
            shows.append(Show(show["name"],show["first_air_date"],show["id"],show["poster_path"]))
            count+=1
        print(count)
    return shows

#Get list of popular shows
def getPopularShows(limit=10):
    movies = getShows("popular", limit)
    return movies 

#Get list of shows that have aired in the past 7 days
def getRunningShows(limit=10):
    movies = getShows("on_the_air", limit)
    return movies 

#Used to run all the categorical calls above, if no type is given it will pick popular shows
def getShows(typeOfLookUp="popular", limit=10):
    page = 0
    count=0
    shows=[]
    
    while limit > count:
        page+=1
        url = "https://api.themoviedb.org/3/tv/"+typeOfLookUp+"?api_key="+os.environ['TMDB_API_KEY']+"&page="+str(page)
        response = requests.request("GET", url)
        responseJSON = response.json()
        
        for show in responseJSON["results"]:
            if count >= limit:
                return shows
            if show["poster_path"]==None:
                show["poster_path"]=""
            else:
                show["poster_path"]="https://www.themoviedb.org/t/p/original" + show["poster_path"]
            shows.append(Show(show["name"],show["first_air_date"],show["id"],show["poster_path"]))
            count+=1
        print(count)
    return shows

"""
tv =  searchShows("Friends", 1)
show = tv[0]
print(show.toString())

main = getFullShowInfoByID(show.tmdbID)
print(main.toString())

populars = getPopularShows()
for popular in populars:
    print(popular.toString())

toprateds = getTopRatedShows()
for toprated in toprateds:
    print(toprated.toString())


trendings = getTrendingShows()
for trending in trendings:
    print(trending.toString())


runnings = getRunningShows()
for running in runnings:
    print(running.toString())

search = searchShows("Lost", 1)
searchFull = getFullShowInfoByID(search[0].tmdbID)
print(searchFull.toString())
"""