import models


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


