#!/usr/bin/python3

import functools
import textwrap

from bs4 import BeautifulSoup
import crayons
import requests


def main():
    response = requests.get(
        'http://speeddemosarchive.com/gamelist/NES.html')
    # Use html5lib because we know this page is poorly
    # formed (no closing li tags)
    soup = BeautifulSoup(response.text, 'html5lib')
    game_list = soup.find('ul')
    games = [a.string for a in game_list.find_all('a')]

    # Set up generator
    color = alternating_color()
    colored = [next(color)(name) for name in games]

    for game in colored:
        print(game, end=' ')
    print()


def alternating_color():
    magenta = functools.partial(crayons.magenta, bold=True)
    cyan = functools.partial(crayons.cyan, bold=True)

    while True:
        for crayon in (magenta, cyan):
            yield crayon


if __name__ == "__main__":
    main()
