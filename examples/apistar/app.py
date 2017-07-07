import sqlite3

from apistar import App, Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes


def games(title='', publisher=''):
    patt = lambda s: '%' + s + '%'
    if title:
        c.execute(
            "SELECT * FROM games WHERE title LIKE ?",
            (patt(title), ))
    elif publisher:
        c.execute(
            "SELECT * FROM games WHERE publisher LIKE ?",
            (patt(publisher), ))
    else:
        c.execute('SELECT * FROM games')
    return c.fetchall()


def get_game(game_id: int):
    c.execute("SELECT * FROM games WHERE id=?", (game_id, ))
    return c.fetchone()


def filter_games_by(key, query):
    key = key.replace(' ', '_')
    result = {
        game for game in GAMES if game[key] and
        query.upper() in game[key].upper()}
    return result


def dict_factory(cursor, row):
    """Turn query results into dictionaries"""
    # https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection.row_factory
    d = {}
    for index, col in enumerate(cursor.description):
        d[col[0]] = row[index]
    return d


routes = [
    Route('/games/', 'GET', games),
    Route('/game/{game_id}/', 'GET', get_game),
    Include('/docs', docs_routes),
    Include('/static', static_routes)]


conn = sqlite3.connect('nes_games.db', check_same_thread=False)
# We want to return results as a serializable dict
# So override the default of returning tuples
conn.row_factory = dict_factory
c = conn.cursor()


app = App(routes=routes)
