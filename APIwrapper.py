import movie
import show
import game
import book


def process_search_request(dcat, dterm, limit=10):
    """
    :param dcat:    the category being searched (movie, game...)
    :param dterm:   the searchterm(s) (hunger games, harry potter, blue...)

    :return:    5 tuple of arrays for categories, titles, years, IDs,
                and cover image links.
    """
    category = []
    title = []
    year = []
    ID = []
    cover = []

    try:
        if (dcat == "movie") or (dcat == ""):
            ret = movie.searchMovies(dterm, limit)
            for mov in ret:
                category.append(mov.category)
                title.append(mov.title)
                year.append(mov.year)
                ID.append(mov.imdbID)
                cover.append(mov.coverPhoto)

        if (dcat == "show") or (dcat == ""):
            ret = show.searchShows(dterm, limit)
            for s in ret:
                category.append(s.category)
                title.append(s.title)
                year.append(s.release_date[:4])
                ID.append(s.tmdbID)
                cover.append(s.coverPhoto)

        if (dcat == "book") or (dcat == ""):
            ret = book.searchBooks(dterm, limit)
            for b in ret:
                category.append(b.category)
                title.append(b.title)
                year.append(b.publishYear)
                ID.append(b.isbn)
                cover.append(b.cover)

        if (dcat == "game") or (dcat == ""):
            ret = game.searchGames(dterm, limit)
            for g in ret:
                category.append(g.category)
                title.append(g.title)
                year.append(g.year)
                ID.append(g.gameID)
                cover.append(g.coverPhoto)

    finally:
        return [category, title, year, ID, cover]


def process_category_request(dcat, dtype, limit=10):
    """
    :param dcat:  category to search (movie, show...)
    :param dtype: top results by type (rating, trending...)

    :return:      5 tuple of arrays for categories, titles, years, IDs,
                  and cover image links.
    """
    category = []
    title = []
    year = []
    ID = []
    cover = []

    try:
        if (dcat == "game"):
            if (dtype == "rating"):
                ret = game.getHighestRatedGames(limit)
                for g in ret:
                    category.append(g.category)
                    title.append(g.title)
                    year.append(g.year)
                    ID.append(g.gameID)
                    cover.append(g.coverPhoto)
            elif (dtype == "anticipation"):
                ret = game.getMostAnticipatedGames(limit)
                for g in ret:
                    category.append(g.category)
                    title.append(g.title)
                    year.append(g.year)
                    ID.append(g.gameID)
                    cover.append(g.coverPhoto)
            elif (dtype == "new"):
                ret = game.getNewlyReleasedGames(limit)
                for g in ret:
                    category.append(g.category)
                    title.append(g.title)
                    year.append(g.year)
                    ID.append(g.gameID)
                    cover.append(g.coverPhoto)
        elif (dcat == "movie"):
            if (dtype == "now playing"):
                ret = movie.getNowPlayingMovies(limit)
                for mov in ret:
                    category.append(mov.category)
                    title.append(mov.title)
                    year.append(mov.year)
                    ID.append(mov.imdbID)
                    cover.append(mov.coverPhoto)
            elif (dtype == "trending"):
                ret = movie.getTrendingMovies(limit)
                for mov in ret:
                    category.append(mov.category)
                    title.append(mov.title)
                    year.append(mov.year)
                    ID.append(mov.imdbID)
                    cover.append(mov.coverPhoto)
            elif (dtype == "rating"):
                ret = movie.getTopRatedMovies(limit)
                for mov in ret:
                    category.append(mov.category)
                    title.append(mov.title)
                    year.append(mov.year)
                    ID.append(mov.imdbID)
                    cover.append(mov.coverPhoto)
            elif (dtype == "upcoming"):
                ret = movie.getUpcomingMovies(limit)
                for mov in ret:
                    category.append(mov.category)
                    title.append(mov.title)
                    year.append(mov.year)
                    ID.append(mov.imdbID)
                    cover.append(mov.coverPhoto)
            elif (dtype == "popular"):
                ret = movie.getPopularMovies(limit)
                for mov in ret:
                    category.append(mov.category)
                    title.append(mov.title)
                    year.append(mov.year)
                    ID.append(mov.imdbID)
                    cover.append(mov.coverPhoto)
        elif (dcat == "book"):
                ret = book.getBestSellers(dtype)
                for mov in ret:
                    category.append(mov.category)
                    title.append(mov.title)
                    year.append(mov.year)
                    ID.append(mov.imdbID)
                    cover.append(mov.coverPhoto)
        elif (dcat == "show"):
            if (dtype == "trending"):
                ret = show.getTrendingShows(limit=limit)
                for mov in ret:
                    category.append(mov.category)
                    title.append(mov.title)
                    year.append(mov.year)
                    ID.append(mov.imdbID)
                    cover.append(mov.coverPhoto)
            elif (dtype == "rating"):
                ret = show.getTopRatedShows(limit)
                for mov in ret:
                    category.append(mov.category)
                    title.append(mov.title)
                    year.append(mov.year)
                    ID.append(mov.imdbID)
                    cover.append(mov.coverPhoto)
            elif (dtype == "popular"):
                ret = show.getPopularShows(limit)
                for mov in ret:
                    category.append(mov.category)
                    title.append(mov.title)
                    year.append(mov.year)
                    ID.append(mov.imdbID)
                    cover.append(mov.coverPhoto)
            elif (dtype == "running"):
                ret = show.getRunningShows(limit)
                for mov in ret:
                    category.append(mov.category)
                    title.append(mov.title)
                    year.append(mov.year)
                    ID.append(mov.imdbID)
                    cover.append(mov.coverPhoto)

    finally:
        return [category, title, year, ID, cover]


def get_info_by_ID(dcat, dID):
    """
    :param dcat:    book, game, movie or show
    :param dID:     isbn, tmdb or game ID to be looked up
    :return:        if successful, 16 tuple dict with the following keys:

        [category, title, year, ID,
        cover, description, creators, rated,
        genres, accessibility, perspectives,
        websites, status, duration, stars]

        else:
        {"category": "error"}
    """
    if (dcat == "game"):
        ret = game.getFullGameInfoByID(gameID=dID)
        return {"category": ret.category, "title": ret.title, "year": ret.year, "ID": ret.gameID,
                "cover": ret.coverPhoto, "description": ret.description, "creators": ret.developers, "rated": ret.rated,
                "genres": ret.genres + ret.gameModes, "accessibility": ret.platforms, "perspectives": ret.perspectives,
                "websites": ret.websites, "status": ret.status, "duration": None, "stars": None}
    if (dcat == "movie"):
        ret = movie.getFullMovieInfoByID(tmdbID=dID)
        return {"category": ret.category, "title": ret.title, "year": ret.year, "ID": ret.tmdbID,
                "cover": ret.coverPhoto, "description": ret.description, "creators": ret.directors, "rating": None,
                "genres": ret.genres, "accessibility": None, "perspectives": None,
                "websites": None, "status": None, "duration": ret.duration, "stars": ret.stars}
    if (dcat == "book"):
        ret = book.getBookByISBN(isbn=dID)
        return {"category": ret.category, "title": ret.title, "year": ret.publishYear, "ID": ret.isbn,
                "cover": ret.cover, "description": ret.description, "creators": ret.authors, "rating": None,
                "genres": ret.genres, "accessibility": ret.languages, "perspectives": None,
                "websites": None, "status": None, "duration": ret.pages, "stars": None}
    if (dcat == "show"):
        ret = show.getFullShowInfoByID(tmdbID=dID)
        return {"category": ret.category, "title": ret.title, "year": ret.release_date[:4], "ID": ret.tmdbID,
                "cover": ret.coverPhoto, "description": ret.description, "creators": ret.creators, "rating": None,
                "genres": ret.genres, "accessibility": ret.networks, "perspectives": None,
                "websites": None, "status": ret.stillAiring, "duration": ret.episodeLength, "stars": None}
    return {"category": "error"}
