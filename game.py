#API CALLER TO PULL GAME DATA FROM IGDB
#Author: Madison Miatke

import requests
import json
import os
from datetime import datetime
from os.path import join, dirname
from dotenv import load_dotenv
from igdb.wrapper import IGDBWrapper
from igdb.igdbapi_pb2 import GameResult

dotenv_path = join(dirname(__file__), "api-keys.env")
load_dotenv(dotenv_path)

#GAME CLASS
class Game:
    def __init__(self,title,year,gameID,coverPhoto,description=None,developers=None,rated=None,genres=None,gameModes=None,platforms=None,perspectives=None,websites=None,status=None):
        self.catergory="game"
        self.title=title
        self.year=year
        self.gameID=gameID
        self.coverPhoto=coverPhoto
        self.description=description
        self.developers=developers
        self.rated=rated
        self.genres=genres
        self.gameModes=gameModes
        self.platforms=platforms
        self.perspectives=perspectives
        self.websites=websites
        self.status=status
    
    def toString(self):
        ret = ("Title: " + str(self.title) + "\n"
        + "Release Year: " + str(self.year) + "\n"
        + "GameID: " + str(self.gameID) + "\n"
        + "Cover Photo: " + str(self.coverPhoto) + "\n"
        + "Description: " + str(self.description) + "\n"
        + "Developers: " + str(self.developers) + "\n"
        + "Rated: " + str(self.rated) + "\n"
        + "Genres: " + str(self.genres) + "\n"
        + "Game Modes: " + str(self.gameModes) + "\n"
        + "Platforms: " + str(self.platforms) + "\n"
        + "Perspectives: " + str(self.perspectives) + "\n"
        + "Websites: " + str(self.websites) + "\n"
        + "Status: " + str(self.status) + "\n")
        return ret

#use api to get full detailed information about a game given its gameID
def getFullGameInfoByID(gameID):

    wrapper= getWrapper()
    byte_array = wrapper.api_request(
                'games',
                'fields id,name,cover,first_release_date,summary,age_ratings,game_modes,genres,involved_companies,platforms,player_perspectives,websites,status; offset 0; where id='+str(gameID)+';'
                )
    
    json = eval(byte_array)[0]
    
    fields = ["id","name","cover","first_release_date","summary","age_ratings","game_modes","genres","involved_companies","platforms","player_perspectives","websites","status"]
    for field in fields:
        if field not in json:
            json[field] = None
    print(json)
    game = Game(
        json["name"],
        unixTimeToYear(json["first_release_date"]),
        json["id"],
        getGameCover(json["cover"]),
        json["summary"],
        getIDNames(json["involved_companies"],"companies"),
        getIDNames(json["age_ratings"],"age_ratings"),
        getIDNames(json["genres"],"genres"),
        getIDNames(json["game_modes"],"game_modes"),
        getIDNames(json["platforms"],"platforms"),
        getIDNames(json["player_perspectives"],"player_perspectives"),
        getIDNames(json["websites"],"websites"),
        json["status"]
    )
    
    return game

#search for a game title using a query
def searchGames(query, limit=10):
    wrapper= getWrapper()
    search_byte_array = wrapper.api_request(
                'games',
                'search "'+query+'"; fields id,name,first_release_date,cover; limit '+str(limit)+';'
                )
    searchJSON = eval(search_byte_array)
    
    fields = ["id","name","cover","first_release_date"]
    
    games = []
    for gameJSON in searchJSON:
        for field in fields:
            if field not in gameJSON:
                gameJSON[field] = None
        
        game = Game(gameJSON["name"],
        unixTimeToYear(gameJSON["first_release_date"]),
        gameJSON["id"],
        getGameCover(gameJSON["cover"]))
        games.append(game)
    
    return games

#call api to get url to cover photo with coverID
def getGameCover(coverID):
    if coverID == None:
        return None    
    
    wrapper= getWrapper()
    cover_byte_array = wrapper.api_request(
                'covers',
                'fields image_id, url; where id='+str(coverID)+';'
                )
    cover_json = eval(cover_byte_array)
    return cover_json[0]["url"]

#call api to get values of dataIDs 
def getIDNames(dataIDs, dataType):
    if dataIDs == None:
        return None
    
    if dataType == "age_ratings":
        field = "rating"
    elif dataType == "websites":
        field = "url"    
    else:
        field = "name"
    
    wrapper= getWrapper()
    
    listID = str(dataIDs)
    listID=listID.replace("[","(")
    listID=listID.replace("]",")")
    print(listID)
    
    byte_array = wrapper.api_request(
                dataType,
                'fields '+field+'; where id = '+listID+';'
                )
    responses = eval(byte_array)

    dataNames=[]
    if responses != []:
        for response in responses:
            if dataType == "age_ratings":
                dataNames.append(getRatingFromID(response[field]))
            else:
                dataNames.append(response[field])
                
    if dataNames == []:
        return None
    
    return dataNames

#get string ratings from a ratingID
def getRatingFromID(ratingID):
    RATINGS = {
        1:"Three",
        2:"Seven",
        3:"Twelve",
        4:"Sixteen",
        5:"Eighteen",
        6:"RP",
        7:"EC",
        8:"E",
        9:"E10",
        10:"T",
        11:"M",
        12:"AO"
    }
    return RATINGS[ratingID]

#get highest rated games
def getHighestRatedGames(limit=10):
    wrapper= getWrapper()
    games_byte_array = wrapper.api_request(
                'games',
                'fields id,name,first_release_date,cover, rating; sort rating desc; where rating != null & rating_count > 500; limit '+str(limit)+';'
                )
    gamesJSON = eval(games_byte_array)
    
    fields = ["id","name","cover","first_release_date"]
    
    games = []
    for gameJSON in gamesJSON:
        for field in fields:
            if field not in gameJSON:
                gameJSON[field] = None
        
        game = Game(gameJSON["name"],
        unixTimeToYear(gameJSON["first_release_date"]),
        gameJSON["id"],
        getGameCover(gameJSON["cover"]))
        games.append(game)
    
    return games

#get most anticipated games that have not been released
def getMostAnticipatedGames(limit=10):
    wrapper= getWrapper()
    games_byte_array = wrapper.api_request(
                'games',
                'fields id,name,first_release_date,cover, hypes; sort hypes desc; where hypes != null & first_release_date = null; limit '+str(limit)+';'
                )
    gamesJSON = eval(games_byte_array)
    
    fields = ["id","name","cover","first_release_date"]
    
    games = []
    for gameJSON in gamesJSON:
        for field in fields:
            if field not in gameJSON:
                gameJSON[field] = None
        
        game = Game(gameJSON["name"],
        None,
        gameJSON["id"],
        getGameCover(gameJSON["cover"]))
        games.append(game)
    
    return games

#get games that were recently released - filtered for games that had an amount of hype
def getNewlyReleasedGames(limit=10):
    wrapper= getWrapper()
    games_byte_array = wrapper.api_request(
                'games',
                'fields id,name,first_release_date,cover; sort first_release_date desc; where hypes > 25 & first_release_date != null; limit '+str(limit)+';'
                )
    gamesJSON = eval(games_byte_array)
    
    fields = ["id","name","cover","first_release_date"]
    
    games = []
    for gameJSON in gamesJSON:
        for field in fields:
            if field not in gameJSON:
                gameJSON[field] = None
        
        game = Game(gameJSON["name"],
        unixTimeToYear(gameJSON["first_release_date"]),
        gameJSON["id"],
        getGameCover(gameJSON["cover"]))
        games.append(game)
    
    return games

#convert unix time to year
def unixTimeToYear(unixTime):
    return datetime.utcfromtimestamp(unixTime).strftime('%Y')

#get wrapper object to make api calls
def getWrapper():
    r = requests.post("https://id.twitch.tv/oauth2/token?client_id="+os.environ['IGDB_CLIENT_ID']+"&client_secret="+os.environ['IGBD_SECRET']+"&grant_type=client_credentials")
    access_token = json.loads(r._content)['access_token']
    wrapper = IGDBWrapper(os.environ['IGDB_CLIENT_ID'], access_token)
    return wrapper


'''Test code
games = searchGames("batman")
for game in games:
    print(game.toString())

fullDetailGame = games[0]
fullDetail = getFullGameInfoByID(fullDetailGame.gameID)
print(fullDetail.toString())

games = getHighestRatedGames()
for game in games:
    print(game.toString())

games = getMostAnticipatedGames()
for game in games:
    print(game.toString())

games = getNewlyReleasedGames()
for game in games:
    print(game.toString())
'''