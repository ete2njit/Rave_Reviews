import models

def register(DB, newUser):
    """
    :param DB:      DB with user table
    :param User:    dict(?) containing users info
    :return:        true if new user created,
                    false if userID already exists in DB or dict did not contain all keys
    """
    try:
        if not DB.session.query(models.User).filter_by(UserID=newUser["UserID"]).first():
            DB.session.add(models.User(
                newUser["UserID"],
                newUser["Username"],
                newUser["Usermail"],
                newUser["Userpfp"],
                newUser["hash"]
            ))
            return True
        return False
    except KeyError:
        return False


def login(DB, returningUser):
    """
    :param DB:                  DB with user table
    :param returningUser:       dict(?) containing users id and hash
    :return:                    dict containing status: OK and user info on success,
                                dict containing status: FAILURE on failure
    """
    ret = DB.session.query(models.User).filter_by(UserID=returningUser["UserID"], hash=returningUser["hash"]).first()

    try:
        return {"status": "OK",
                "UserID": ret["UserID"],
                "Username": ret["Username"],
                "Usermail": ret["Usermail"],
                "Userpfp": ret["Userpfp"]}
    except KeyError:
        return {"status": "FAILURE"}


def getProfile(DB, userID):
    """
    :param DB:              DB with user table
    :param userID:          ID of user profile to look up
    :return:                status: OK and user data if retrieve succeeded
                            status: FAILURE otherwise
    """
    ret = DB.session.query(models.User).filter_by(UserID=userID).first()

    try:
        return {"status": "OK",
                "Username": ret["Username"],
                "Usermail": ret["Usermail"],
                "Userpfp": ret["Userpfp"]}
    except KeyError:
        return {"status": "FAILURE"}


def getReviews(DB, pageID):
    """
    :param DB:      DB with reviews table
    :param pageID:  isbn, tmdb or game ID to be looked up

    :return:    3 tuple of arrays for userID(author), rating, review text
    """
    userIDs = []
    ratings = []
    reviews = []

    for review in DB.session.query(models.Review).filter_by(PageID=pageID).all():
        userIDs.append(review.UserID)
        ratings.append(review.Rating)
        reviews.append(review.ReviewText)

    return [userIDs, ratings, reviews]


def writeReview(DB, pageID, userID, rating, review):
    """
    :param DB:      DB that contains review table
    :param pageID:  ID of the show, movie, game or book being reviewed
    :param userID:  user leaving review
    :param rating:  given rating
    :param review:  text content of review
    :return:        none
    """

    DB.session.add(models.Review(pageID, userID, rating, review))
    DB.session.commit()


