#!/usr/bin/python3

import functools
import textwrap

from bs4 import BeautifulSoup
import crayons
from fuzzywuzzy import process
import requests


def main():
    sda_games = set(get_sda_games())
    print('Found {} games on SDA'.format(len(sda_games)))
    all_games = set(get_all_nes_games())
    print('Found {} games on Wikipedia'.format(len(all_games)))
    fuzzy_sda_games = [
        (game, *process.extractOne(game, all_games)) for
        game in sda_games]
    matched_sda_games = {
        g[1] for g in fuzzy_sda_games if g[2] >= 90}
    unmatched_sda_games = (g for g in fuzzy_sda_games if g[2] < 90)

    # Set up generator
    color = alternating_color()

    # Output!
    no_records = all_games - matched_sda_games
    colored = [next(color)(name) for name in no_records]
    print(
        'There are {} games with no records on SDA! '
        'Go grind!'.format(len(no_records)))
    print('Games that could be matched:')

    for game in colored:
        print(game, end=' ')
    print()

    print("Games that couldn't be matched:")
    for game in unmatched_sda_games:
        print('{}: Best Match: {} Score: {}'.format(*game))


def get_sda_games():
    response = requests.get(
        'http://speeddemosarchive.com/gamelist/NES.html')
    # Use html5lib because we know this page is poorly
    # formed (no closing li tags)
    soup = BeautifulSoup(response.text, 'html5lib')
    game_list = soup.find('ul')
    return [a.string for a in game_list.find_all('a')]


def get_all_nes_games():
    response = requests.get(
        'https://en.wikipedia.org/wiki/'
        'List_of_Nintendo_Entertainment_System_games')
    # HTML is not broken, so Use lxml parser,
    # which is a whole lot faster.
    soup = BeautifulSoup(response.text, 'lxml')
    game_list = soup.find('table').find_all('tr')[2:]
    return [tr.find('a').string for tr in game_list]


def alternating_color():
    magenta = functools.partial(crayons.magenta, bold=True)
    cyan = functools.partial(crayons.cyan, bold=True)

    while True:
        for crayon in (magenta, cyan):
            yield crayon


if __name__ == "__main__":
    main()
