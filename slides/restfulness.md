# <span style='color: #3DE9FE'>REST</span>fulness
## What does it mean to be *RESTful*?
+++
# <span style='color: #3DE9FE'>RE</span>presentational
# <span style='color: #3DE9FE'>S</span>tate
# <span style='color: #3DE9FE'>T</span>ransfer
+++
# <span style='color: #3DE9FE'>RE</span>presentational
REST is about exposing *resources*.

Note:
- Resources could be anything; files, concepts, (computers in your management tool, status updates on twitter)
- The REST API abstracts the storage of resources from the interface for getting at them.
- The data exchanged is representational, meaning it may be in multiple formats that do not
  resemble the native storage (e.g. XML or JSON vs. a SQL table row).
+++
## Example: http://api.giphy.com/v1/gifs/<span style='color: #FA00C0'>qRryuPIunLS1O</span>
(Get a GIF by its ID)
+++?code=examples/giphy/one_gif.json
@[2-4]
@[19-32]

+++
# <span style='color: #3DE9FE'>S</span>tate
+++
# <span style='color: #3DE9FE'>T</span>ransfer

# Requests
# Responses
# Status codes
Note:
Rest is not a protocol; just an architectural style
http://myserver.com/catalog/item/1729
but the REST architecture does not require these “pretty URLs”. A GET request with a parameter

http://myserver.com/catalog?item=1729
