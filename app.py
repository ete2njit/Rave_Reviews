# app.py
import os

from os.path import join, dirname
from dotenv import load_dotenv

import movie
import show
import game
import book

import flask
import flask_socketio
import flask_sqlalchemy


# Channel names
SEARCH_REQUEST_CHANNEL = "search request"
SEARCH_RESPONSE_CHANNEL = "search response"
#


APP = flask.Flask(__name__)

SOCKETIO = flask_socketio.SocketIO(APP)
SOCKETIO.init_app(APP, cors_allowed_origins="*")

dotenv_path = join(dirname(__file__), "pg.env")
load_dotenv(dotenv_path)


APP.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URI"]

DB = flask_sqlalchemy.SQLAlchemy(APP)
DB.init_app(APP)
DB.app = APP
import models

DB.create_all()
DB.session.commit()


@SOCKETIO.on('connect')
def on_connect():
    print('Someone connected!')
    SOCKETIO.emit('connected', {
        'test': 'Connected'
    })


@SOCKETIO.on('disconnect')
def on_disconnect():
    print('Someone disconnected!')


@SOCKETIO.on(SEARCH_REQUEST_CHANNEL)
def on_search_request(data):
    if "category" not in data:
        print("something went wrong")
        return

    dcat = data["category"]
    dterm = data["searchTerm"]

    print("processing search request: " + dcat + ", " + dterm)

    category = []
    title = []
    year = []
    ID = []
    cover = []

    if (dcat == "movie") or (dcat == ""):
        ret = movie.searchMovies(dterm)
        for mov in ret:
            category.append(mov.category)
            title.append(mov.title)
            year.append(mov.year)
            ID.append(mov.imdbID)
            cover.append(mov.coverPhoto)

    if (dcat == "show") or (dcat == ""):
        ret = show.searchShows(dterm)
        for s in ret:
            category.append(s.category)
            title.append(s.title)
            year.append(s.release_date[:4])
            ID.append(s.tmdbID)
            cover.append(s.coverPhoto)

    if (dcat == "book") or (dcat == ""):
        ret = book.searchBooks(dterm)
        for b in ret:
            category.append(b.category)
            title.append(b.title)
            year.append(b.publishYear)
            ID.append(b.isbn)
            cover.append(b.cover)

    if (dcat == "game") or (dcat == ""):
        ret = game.searchGames(dterm)
        for g in ret:
            category.append(g.category)
            title.append(g.title)
            year.append(g.year)
            ID.append(g.gameID)
            cover.append(g.coverPhoto)

    SOCKETIO.emit(
        SEARCH_RESPONSE_CHANNEL,
        {
            "category": category,
            "title": title,
            "year": year,
            "ID": ID,
            "cover": cover,
        },
    )

    print("finished processing search request")


@APP.route('/')
def index():
    return flask.render_template("index.html")


if __name__ == '__main__':
    SOCKETIO.run(
        APP,
        host=os.getenv('IP', 'localhost'),
        port=int(os.getenv('PORT', 8080)),
        debug=True
    )
