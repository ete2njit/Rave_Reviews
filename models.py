# models.py
import flask_sqlalchemy
from app import DB


class Page(DB.Model):
    Title = DB.Column(DB.String(256), primary_key=True)
    Subtitle = DB.Column(DB.String(256), primary_key=True)
    Type = DB.Column(DB.String(256), primary_key=True)

    PageID = DB.Column(DB.Integer, autoincrement=True)
    ReleaseDate = DB.Column(DB.DateTime())

    def __init__(self, Title, Subtitle, Type, PageID, ReleaseDate):
        self.Title = Title
        self.Subtitle = Subtitle
        self.Type = Type
        self.PageID = PageID
        self.ReleaseDate = ReleaseDate


class PageGenre:
    PageID = DB.Column(DB.Integer, primary_key=True)
    Genre = DB.Column(DB.String(256), primary_key=True)

    def __init__(self, PageID, Genre):
        self.PageID = PageID
        self.Genre = Genre


#class Review:
#    PageID = DB.Column(DB.Integer, primary_key=True)
