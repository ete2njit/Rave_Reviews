# models.py
import flask_sqlalchemy
from app import DB


class Page(DB.Model):
    Title = DB.Column(DB.String(256), primary_key=True)
    Subtitle = DB.Column(DB.String(256), primary_key=True)
    Type = DB.Column(DB.String(256), primary_key=True)

    ReleaseDate = DB.Column(DB.DateTime())
    PageID = DB.Column(DB.Integer, autoincrement=True)

    def __init__(self, Title, Subtitle, Type, ReleaseDate=None):
        self.Title = Title
        self.Subtitle = Subtitle
        self.Type = Type
        self.ReleaseDate = ReleaseDate


class PageGenre(DB.Model):
    PageID = DB.Column(DB.Integer, primary_key=True, autoincrement=False)
    Genre = DB.Column(DB.String(256), primary_key=True)

    def __init__(self, PageID, Genre):
        self.PageID = PageID
        self.Genre = Genre


class Review(DB.Model):
    PageID = DB.Column(DB.Integer, primary_key=True, autoincrement=False)
    UserID = DB.Column(DB.String(256), primary_key=True)

    Rating = DB.Column(DB.Float, nullable=False)
    ReviewText = DB.Column(DB.String(8192), nullable=False)
    ReviewID = DB.Column(DB.Integer, autoincrement=True)

    def __init__(self, PageID, UserID, Rating, ReviewText):
        self.PageID = PageID
        self.UserID = UserID
        self.Rating = Rating
        self.ReviewText = ReviewText


class Like(DB.Model):
    ReviewID = DB.Column(DB.Integer, primary_key=True, autoincrement=False)
    UserID = DB.Column(DB.String(256), primary_key=True)

    def __init__(self, ReviewID, UserID):
        self.ReviewID = ReviewID
        self.UserID = UserID


class User(DB.Model):
    UserID = DB.Column(DB.String(256), primary_key=True)

    Username = DB.Column(DB.String(512), nullable=False)
    Userpfp = DB.Column(DB.String(256), nullable=False)

    def __init__(self, UserID, Username, Userpfp):
        self.UserID = UserID
        self.Username = Username
        self.Userpfp = Userpfp
