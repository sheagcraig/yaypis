#!/usr/bin/env python3


import io
import json
import os

import requests
from requests_oauthlib import OAuth1Session
from PIL import Image


ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')


def main():
    # Use the Twitter Developer site to create an application and get
    # your tokens.
    # Make sure to provide access token and consumer key via sourcing the
    # secrets file!
    oauth = OAuth1Session(
        CONSUMER_KEY, client_secret=CONSUMER_SECRET,
        resource_owner_key=ACCESS_TOKEN,
        resource_owner_secret=ACCESS_TOKEN_SECRET)
    taco_response = oauth.get(
        'https://api.twitter.com/1.1/search/tweets.json?q=tacos&filter=images')
    taco_tweets = taco_response.json()
    taco_images = get_images(taco_tweets)
    images = [create_image(url) for url in taco_images]
    show_images(images)
    save_images(images, 'tacos')


def get_images(statuses):
    tweets = statuses['statuses']
    return {img.get('media_url') for tweet in tweets for
            img in tweet['entities'].get('media', [])}


def create_image(url):
    response = requests.get(url)
    img_stream = io.BytesIO(response.content)
    return Image.open(img_stream)


def save_images(images, name_prefix, basedir=os.getcwd()):
    pad = len(str(len(images)))
    for index, image in enumerate(images):
        image_path = os.path.join(
            basedir, '{0}_{1:0{2}d}.png'.format(name_prefix, index, pad))
        image.save(image_path)


def show_images(images):
    for image in images:
        image.show()


if __name__ == "__main__":
    main()