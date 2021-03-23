import movie
import show
import game
import book


def process_search_request(dcat, dterm):
    """
    :param dcat:    the category being searched (movie, game...)
    :param dtype:   the searchterm(s) (hunger games, harry potter, blue...)

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

    finally:
        return [category, title, year, ID, cover]
