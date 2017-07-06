# Create a REST API for existing services
+++
# APIStar
https://github.com/tomchristie/apistar

+++
```shell
apistar new . --layout minimal
```

+++?code=examples/apistar/app.py
@[3-5]
@[15-19]
@[8-12]

+++
```shell
apistar run
```
+++
```python
>>> import json
>>> import requests
>>> response = requests.get('http://localhost:8080/?=mario')
>>> print(json.dumps(response.json(), indent=4))
{
    "games": [
        {
            "title": "Dr. Mario",
            "release date": "October 1990",
            "publisher": "Nintendo"
        },
        {
            "title": "Mario Bros.",
            "release date": "June 1986",
            "publisher": "Nintendo"
        },
        {
            "title": "Mario Is Missing!",
            "release date": "July 1993",
            "publisher": "Mindscape"
        },
        {
            "title": "Mario's Time Machine",
            "release date": "June 1994",
            "publisher": "Mindscape"
        },
        {
            "title": "Super Mario Bros.",
            "release date": "October 18, 1985",
            "publisher": "Nintendo"
        },
        {
            "title": "Super Mario Bros./Duck Hunt",
            "release date": "November 1988",
            "publisher": "Nintendo"
        },
        {
            "title": "Super Mario Bros./Duck Hunt/World Class Track Meet",
            "release date": "December 1990",
            "publisher": "Nintendo"
        },
        {
            "title": "Super Mario Bros./Tetris/Nintendo World Cup",
            "release date": "November 1988",
            "publisher": "Nintendo"
        },
        {
            "title": "Super Mario Bros. 2",
            "release date": "October 10, 1988",
            "publisher": "Nintendo"
        },
        {
            "title": "Super Mario Bros. 3",
            "release date": "February 12, 1990",
            "publisher": "Nintendo"
        }
    ]
}
```
@[1-2]
@[3-4]
@[41-55]

+++?image=assets/apistar_docs.png&size=contain
+++?image=assets/apistar_interact.png&size=contain

+++
# Flask
+++
# Munki client manifest service
