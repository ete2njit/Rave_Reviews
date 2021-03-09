# app.py
import os
import flask
from os.path import join, dirname
from dotenv import load_dotenv

import flask_socketio
import flask_sqlalchemy

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