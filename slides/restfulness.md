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

Note:
This gif is uniquely identified by its gif ID, which is important in how we address it.

+++?code=examples/giphy/one_gif.json
@[2-4]
@[19-32]

Note:
This JSON is a *representation* of the gif resource stored with Giphy.

+++
# <span style='color: #3DE9FE'>S</span>tate
# <span style='color: #3DE9FE'>T</span>ransfer

Note:

REST should be stateless. All request from the client contains all of the information necessary to
service the request; the server doesn't have to track the client (as opposed to say, FTP where
things like CWD are tracked).

A truly restful service provides the equivalent of hyperlinks to give the client an idea of where
it can "go" from each response.

However, "State transfer" means that the embedded links provide a means for the client to transfer
between "application states".

Where a lot of web services fail to be truly RESTful is that they don't provide hyperlinks.

Therefore, we're not super worried about this part of it.

+++
Rest is not a protocol; just an architectural style

Example: Which is "correct"?
- http://myserver.com/catalog/item/1729
- http://myserver.com/catalog?item=1729

---
## What does it mean *practically* to be *RESTful*?

- Resources are accessed through HTTP requests to a collection of URLs.
	- http://instagrambookfacetweets.com/api/cat_videos/
- These resources are *represented*, for our examples at least, as JSON or XML.
- We can also create and update resources using the representations provided.

+++?image=assets/request_flowchart.jpg&size=contain
+++
## Example

- We make a HTTP GET request to the computers endpoint to get a list of all computers.
- We parse the resulting XML
- We find a computer we're interested in manipulating, and change something (asset tag?)
- We PUT that record back to that computer's unique URL, and the server responds wether it worked or not.
- Etc.

---
What do we need from our API? What do we want to *do*?
+++
# CRUD
-  <span style='color: #3DE9FE'>C</span>reate
-  <span style='color: #3DE9FE'>R</span>ead
-  <span style='color: #3DE9FE'>U</span>pdate
-  <span style='color: #3DE9FE'>D</span>elete

Note:
The major functions needed for manipulating data in persistent storage (i.e. a database/webapp)

+++
# BREAD
-  <span style='color: #3DE9FE'>B</span>rowse
-  <span style='color: #3DE9FE'>R</span>ead
-  <span style='color: #3DE9FE'>E</span>dit
-  <span style='color: #3DE9FE'>A</span>dd
-  <span style='color: #3DE9FE'>D</span>elete

+++
# CRAP
-  <span style='color: #3DE9FE'>C</span>reate
-  <span style='color: #3DE9FE'>R</span>etrieve
-  <span style='color: #3DE9FE'>A</span>lter
-  <span style='color: #3DE9FE'>P</span>urge
<br/>
<img src="assets/tshirt.jpg" alt='Nice shirt' style='width: 200px;' />

+++

# Requests
Note:
Talk about HTTP methods
Talk about accept header
+++
# Responses
Note:
Remember to talk about caching.
Content-type
+++
# Status codes
