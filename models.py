# models.py

from app import DB


class Page(DB.Model):
    PageID = DB.Column(DB.String(256), primary_key=True)

    Title = DB.Column(DB.String(256))
    Subtitle = DB.Column(DB.String(256))
    Type = DB.Column(DB.String(256))
    Year = DB.Column(DB.Integer())

    def __init__(self, PageID, Title, Subtitle, Type, Year):
        self.PageID = PageID
        self.Title = Title
        self.Subtitle = Subtitle
        self.Type = Type
        self.Year = Year


class PageGenre(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    PageID = DB.Column(DB.String(256), DB.ForeignKey("page.PageID"))
    Genre = DB.Column(DB.String(256))

    DB.relationship(Page, backref=DB.backref("genres"))

    def __init__(self, PageID, Genre):
        self.PageID = PageID
        self.Genre = Genre


class User(DB.Model):
    UserID = DB.Column(DB.String(256), primary_key=True)

    Username = DB.Column(DB.String(512), nullable=False)
    Usermail = DB.Column(DB.String(512), nullable=False)
    Userpfp = DB.Column(DB.String(256), nullable=False)

    hash = DB.Column(DB.String(512), nullable=False)

    def __init__(self, UserID, Username, Usermail, Userpfp, hash):
        self.UserID = UserID
        self.Username = Username
        self.Usermail = Usermail
        self.Userpfp = Userpfp
        self.hash = hash


class Review(DB.Model):
    ReviewID = DB.Column(DB.Integer, primary_key=True)

    PageID = DB.Column(DB.String(256), DB.ForeignKey("page.PageID"))
    UserID = DB.Column(DB.String(256), DB.ForeignKey("user.UserID"))

    Rating = DB.Column(DB.Float, nullable=False)
    ReviewText = DB.Column(DB.String(8192), nullable=False)

    DB.relationship(Page, backref=DB.backref("reviews"))
    DB.relationship(User, backref=DB.backref("reviews"))

    def __init__(self, PageID, UserID, Rating, ReviewText):
        self.PageID = PageID
        self.UserID = UserID
        self.Rating = Rating
        self.ReviewText = ReviewText


class Like(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)

    ReviewID = DB.Column(DB.Integer, DB.ForeignKey("review.ReviewID"))
    UserID = DB.Column(DB.String(256), DB.ForeignKey("user.UserID"))

    DB.relationship(Review, backref=DB.backref("likes"))
    DB.relationship(User, backref=DB.backref("likes"))

    def __init__(self, ReviewID, UserID):
        self.ReviewID = ReviewID
        self.UserID = UserID



