import json

from apistar import App, Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes


def games(name=''):
    result = [
        game for game in GAMES if game['title'] and
        name.upper() in game['title'].upper()]
    return {'games': result}


routes = [
    Route('/', 'GET', games),
    Include('/docs', docs_routes),
    Include('/static', static_routes)
]

with open('nes_games.json') as ifile:
    GAMES = json.load(ifile)

app = App(routes=routes)
