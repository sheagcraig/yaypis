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
# <span style='color: #3DE9FE'>T</span>ransfer
Note:

TODO: This needs to be written and practiced so as to make sense quickly. TL;DR version, don't
worry too much about this part. Pragmatically, we can skip understanding it.

REST should be stateless. All request from the client contains all of the information necessary to
service the request; the server doesn't have to track the client (as opposed to say, FTP where
things like CWD are tracked).

Where a lot of web services fail to be truly RESTful is that they don't provide hyperlinks.

A truly restful service provides the equivalent of hyperlinks to give the client an idea of where
it can "go" from each response.

However, "State transfer" means that the embedded links provide a means for the client to transfer
between "application states".
+++
# Requests
+++
# Responses
Note:
Remember to talk about caching.
+++
# Status codes
Note:
Rest is not a protocol; just an architectural style

but the REST architecture does not require these “pretty URLs”. A GET request with a parameter
http://myserver.com/catalog/item/1729
http://myserver.com/catalog?item=1729


