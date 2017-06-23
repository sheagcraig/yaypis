---?image=assets/newwave.jpg
---
## yAyPIs
### ( <span style='color: #3DE9FE'>Y</span><span style='color: #FA00C0'>A</span><span style='color: #3DE9FE'>Y</span> + APIs )
### Working with REST APIs in Python

---

#  What we're covering:

+++

- Preamble: Why it’s important to have fun <!-- .element: class="fragment" -->
- Restfulness                              <!-- .element: class="fragment" -->
- Making requests <!-- .element: class="fragment" -->
- Handling responses<!-- .element: class="fragment" -->
- Python API frameworks for services<!-- .element: class="fragment" -->
- Generic API wrappers <!-- .element: class="fragment" -->
- Create a REST API for existing services <!-- .element: class="fragment" -->
- Design and implementation of API wrappers <!-- .element: class="fragment" -->

---
# Preamble
## Why it’s important to have fun!

Note:
Chances are extremely good that you'll be completely bogged down by design decisions and worry about
"doing it right" if you start with something critical for your organization. Or maybe you don't have
any ideas for things to do to help you at your job (yet).

+++?image=assets/mab.jpg&size=cover

## Code is <span style='color: #3DE9FE'>*art*</span>

Play with these:
- Image processing: https://github.com/python-pillow/Pillow 
- More image processing: http://scikit-image.org/
- Computer Vision! Machine learning and other magic: http://opencv.org
- Interactive data visualization hotness: https://github.com/bokeh/bokeh
- Shred the English language: http://www.nltk.org 

+++

## Code is <span style='color: #3DE9FE'>*art*</span>

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

---
# Example
Note:
TODO just demonstrate something cool with a single request; like querying twitters?

---?include=slides/api.md

---?include=slides/restfulness.md

---?include=slides/requests.md

---?include=slides/responses.md

---?include=slides/example_frameworks.md

---?include=slides/generic_wrappers.md

---?include=slides/api_creation.md

---?include=slides/api_wrapping.md