#!/usr/bin/env python3


import io
import os

import requests
from PIL import Image


API_KEY = os.getenv('API_KEY')


def main():
    # Make sure to provide API key via sourcing the secrets file!
    params = {'q': 'tacos', 'api_key': API_KEY, 'limit': 1}
    response = requests.get("http://api.giphy.com/v1/gifs/search", params=params)
    result = response.json()
    import pdb; pdb.set_trace()
    url = result['data'][0]['images']['original']['url']
    gif = get_gif(url)
    gif.save(os.path.join(os.getcwd(), 'taco.gif'), save_all=True)


def get_gif(url):
    response = requests.get(url)
    img_stream = io.BytesIO(response.content)
    return Image.open(img_stream)


if __name__ == "__main__":
    main()