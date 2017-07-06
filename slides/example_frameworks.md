# Frameworks for your favorite services

+++

| Service | Python Package |
| --- | --- |
| Instagram | https://github.com/LevPasha/Instagram-API-python |
| Twitter | https://github.com/bear/python-twitter, https://github.com/tweepy/tweepy |
| Spotify | https://github.com/plamere/spotipy |
| Strava | https://github.com/hozn/stravalib |
| Facebook | https://github.com/mobolic/facebook-sdk |
| Google Everything | https://developers.google.com/api-client-library/python/  |

+++
# Spotify
## Actually Random

+++
## Actually Random Overview

1. Use OAuth2 to authenticate user and grant permission to app
1. Get user's playlists and display
1. User selects playlist; get all tracks from playlist
1. Shuffle and display
1. User saves; Create new playlist, add randomized tracks


+++?code=examples/actually_random/actually_random.py
@[53-54]
@[168]
@[230-233]
@[239-243]
@[116-120]
@[129-131]
@[133-140]

+++?image=examples/actually_random/screenshots/playlists.png&size=contain
+++?image=examples/actually_random/screenshots/playlist.png&size=contain

+++
# Strava
## http://www.marcellobrivio.com/projects/strava-toolbox/
+++?image=assets/the_badger1.png&size=contain
+++?image=assets/the_badger2.png&size=contain

+++
# Google ~~Image Search~~ Custom Search Engine
## Triptych

+++
## Triptych Overview

1. Use system dictionary to generate random search
1. Perform search for images for each random word
1. Randomly choose one of the results for each.
1. Generate triptych from final images

+++?code=examples/chops/triptych.py
@[34-35]
@[133-136]

+++?image=examples/chops/examples/triptych.jpg&size=contain
+++?image=examples/chops/examples/triptych2.jpg&size=contain
