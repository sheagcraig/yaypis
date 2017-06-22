#!/usr/bin/env python3


import io
import json
import os

import oauth2
import requests
from PIL import Image


ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.getenv('ACCESS_TOKEN_SECRET')
CONSUMER_KEY = os.getenv('CONSUMER_KEY')
CONSUMER_SECRET = os.getenv('CONSUMER_SECRET')


def main():
    # Make sure to provide access token and consumer key via sourcing the secrets file!
    taco_response = oauth_req(
        'https://api.twitter.com/1.1/search/tweets.json?q=tacos&filter=images', ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET)
    taco_tweets = json.loads(taco_response)
    taco_images = get_images(taco_tweets)
    images = [create_image(url) for url in taco_images]
    show_images(images)
    save_images(images, 'tacos')


def oauth_req(url, key, secret, http_method="GET", post_body=b'', http_headers=None):
    consumer = oauth2.Consumer(key=CONSUMER_KEY, secret=CONSUMER_SECRET)
    token = oauth2.Token(key=key, secret=secret)
    client = oauth2.Client(consumer, token)
    resp, content = client.request(url, method=http_method, body=post_body, headers=http_headers)
    return content


def get_images(statuses):
    tweets = statuses['statuses']
    return {img.get('media_url') for tweet in tweets for img in tweet['entities'].get('media', [])}


def create_image(url):
    response = requests.get(url)
    img_stream = io.BytesIO(response.content)
    return Image.open(img_stream)


def save_images(images, name_prefix, basedir=os.getcwd()):
    pad = len(str(len(images)))
    for index, image in enumerate(images):
        image_path = os.path.join(basedir, '{0}_{1:0{2}d}.png'.format(name_prefix, index, pad))
        image.save(image_path)


def show_images(images):
    for image in images:
        image.show()


if __name__ == "__main__":
    main()