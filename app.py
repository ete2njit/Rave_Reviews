# app.py
import os

from os.path import join, dirname
from dotenv import load_dotenv

from APIs import APIwrapper
import DBwrapper

import flask
import flask_socketio
import flask_sqlalchemy


# Channel names
SEARCH_REQUEST_CHANNEL = "search request"
SEARCH_RESPONSE_CHANNEL = "search response"
CATEGORY_REQUEST_CHANNEL = "category request"
CATEGORY_RESPONSE_CHANNEL = "category response"
INFO_BY_ID_REQUEST_CHANNEL = "info by id request"
INFO_BY_ID_RESPONSE_CHANNEL = "info by id response"
GET_REVIEWS_REQUEST_CHANNEL = "get reviews request"
GET_REVIEWS_RESPONSE_CHANNEL = "get reviews response"
WRITE_REVIEW_CHANNEL = "write review"
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

DB.create_all()
DB.session.commit()


@SOCKETIO.on('connect')
def on_connect():
    print('Someone connected!')
    SOCKETIO.emit('connected', {
        'test': 'Connected'
    }, room=flask.request.sid)


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
    try:
        limit = data["limit"]
    except KeyError:
        limit = 10

    print("processing search request: " + dcat + ", " + dterm)

    [category, title, year, ID, cover] = APIwrapper.process_search_request(dcat, dterm, limit)

    SOCKETIO.emit(
        SEARCH_RESPONSE_CHANNEL,
        {
            "category": category,
            "title": title,
            "year": year,
            "ID": ID,
            "cover": cover,
        }, room=flask.request.sid
    )

    print("finished processing search request")


@SOCKETIO.on(CATEGORY_REQUEST_CHANNEL)
def on_category_request(data):
    dcat = data["category"]
    dterm = data["searchTerm"]
    try:
        limit = data["limit"]
    except KeyError:
        limit = 10

    print("processing search request: " + dcat + ", " + dterm)

    [category, title, year, ID, cover] = APIwrapper.process_category_request(dcat, dterm, limit)

    SOCKETIO.emit(
        CATEGORY_RESPONSE_CHANNEL,
        {
            "category": category,
            "title": title,
            "year": year,
            "ID": ID,
            "cover": cover,
        }, room=flask.request.sid
    )


@SOCKETIO.on(INFO_BY_ID_REQUEST_CHANNEL)
def on_id_request(data):
    dcat = data["category"]
    dID = data["ID"]


    ret = APIwrapper.get_info_by_ID(dcat, dID)

    SOCKETIO.emit(
        INFO_BY_ID_RESPONSE_CHANNEL,
        {
            "category": ret["category"],
            "title": ret["title"],
            "year": ret["year"],
            "ID": ret["ID"],
            "cover": ret["cover"],
            "description": ret["description"],
            "creators": ret["creators"],
            "rated": ret["rated"],
            "genres": ret["genres"],
            "accessibility": ret["accessibility"],
            "perspectives": ret["perspectives"],
            "websites": ret["websites"],
            "status": ret["status"],
            "duration": ret["duration"],
            "stars": ret["stars"],
        }, room=flask.request.sid
    )


@SOCKETIO.on(GET_REVIEWS_REQUEST_CHANNEL)
def get_review(data):
    [userIDs, ratings, reviews] = DBwrapper.getReviews(DB, data["ID"])

    SOCKETIO.emit(
        GET_REVIEWS_RESPONSE_CHANNEL,
        {
            "userIDs": userIDs,
            "ratings": ratings,
            "reviews": reviews,
        }, room=flask.request.sid
    )


@SOCKETIO.on(WRITE_REVIEW_CHANNEL)
def write_review(data):
    DBwrapper.writeReview(DB, data["ID"], data["userID"], data["rating"], data["review"])


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
