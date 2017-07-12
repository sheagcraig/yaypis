---?image=assets/newwave.jpg
---
## yAyPIs
### ( **Y**<em>A</em>**Y** + APIs )
### Working with REST APIs in Python

---
# Preamble
## Why it’s important to have fun!

Note:
Chances are extremely good that you'll be completely bogged down by design decisions and worry about
"doing it right" if you start with something critical for your organization. Or maybe you don't have
any ideas for things to do to help you at your job (yet).

+++?image=assets/mab.jpg&size=cover

## Code is **art**

Play with these:
- Image processing: https://github.com/python-pillow/Pillow 
- More image processing: http://scikit-image.org/
- Computer Vision! Machine learning and other magic: http://opencv.org
- Interactive data visualization hotness: https://github.com/bokeh/bokeh
- Shred the English language: http://www.nltk.org 

+++

## Code is **art**

Send them here:
- http://turbulence.org 
- https://anthology.rhizome.org 
- https://creators.vice.com/en_us/topic/new-media-art 
- http://www.isea-web.org 
- https://www.aec.at/about/en/

Note:
What about doing something completely locally and then just automating an update to Twitter or Instagram?

+++
# Challenge 

Come up with a clever toy-project using web services.
Example: 
<span style='color: #3DE9FE'>*Grab* all of the taco tweets, *tokenize* the text, and *tag* to get the adjectives, then *visualize* how people are *describing* tacos.</span>

Note:
More experienced audience come up with a cool idea by the end of the talk

---?image=assets/lu-xiaojun-2012-olympcs.jpg&size=contain

Note:
Triage concept in training: Only focus on one thing at a time, whatever is most important.

---
# Example
+++?code=examples/giphy/giphy_basic.py
@[1]
@[7-8] @[16-17]
@[18]
+++?code=examples/giphy/results.json
@[2]
@[20]
@[121-131]
+++?code=examples/giphy/giphy_basic.py
@[19-21]

+++
![Tacos!](examples/giphy/taco.gif)

---
# Setup
Prerequisite: Install python3 from python.org (and then install certifi...)

```shell
$ cd /path/to/project
$ python3 -m venv venv_folder
$ source venv_folder/bin/activate
$ pip3 install -r requirements.txt
```

Read this:
http://docs.python-guide.org/en/latest/

---?include=slides/api.md
---?include=slides/restfulness.md
---?include=slides/general_requests.md
---?include=slides/requests.md
---?include=slides/xml.md
---?include=slides/json.md
---?include=slides/scraping.md
---?include=slides/example_frameworks.md
---?include=slides/generic_wrappers.md
---?include=slides/api_creation.md