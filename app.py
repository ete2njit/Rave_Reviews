# app.py
import os
import flask
from os.path import join, dirname
from dotenv import load_dotenv

import movie

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

    if data["category"] != "movie":
        print("only movies supported atm")
        return

    ret = movie.searchMovies(data["searchTerm"])

    for mov in ret:
        print(mov.toString())


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
