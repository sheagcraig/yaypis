# **REST**fulness
## What does it mean to be **RESTful**?
+++
# **RE**presentational
# **S**tate
# **T**ransfer
+++
# **RE**presentational
REST is about exposing *resources*.

Note:
- Resources could be anything; files, concepts, (computers in your management tool, status updates on twitter)
- The REST API abstracts the storage of resources from the interface for getting at them.
- The data exchanged is representational, meaning it may be in multiple formats that do not
  resemble the native storage (e.g. XML or JSON vs. a SQL table row).
+++
## Example: http://api.giphy.com/v1/gifs/<em>qRryuPIunLS1O</em>
(Get a GIF by its ID)

Note:
This gif is uniquely identified by its gif ID, which is important in how we address it.

+++?code=examples/giphy/one_gif.json
@[2-4]
@[19-32]

Note:
This JSON is a *representation* of the gif resource stored with Giphy.

+++
# **S**tate
# **T**ransfer

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

- Resources are mapped to a collection of URLs |
	- Resources are uniquely identified. |
	- Collection http://instagrambookfacetweets.com/api/cat_videos/ |
	- Individual http://instagrambookfacetweets.com/api/cat_videos/45244029342342 |

+++
## What does it mean *practically* to be *RESTful*?
- Resources are *represented* as JSON or XML.
- We specify the action we wish to perform using HTTP methods (GET, POST, PUT, DELETE).
- The status code of the response represents type of success or failure.
	- *200* = **YAY**

+++?image=assets/request_flowchart.jpg&size=contain
+++
## Example

- We make a **HTTP GET request** to the computers endpoint to get a list of all computers.
- We *parse* the resulting XML
- We **find** a computer we're interested in manipulating, and *change* something (asset tag?)
- We **PUT** that record back to that computer's unique URL, and the server *responds* wether it worked or not.
- Etc.

---
What do we need from our API? What do we want to *do*?
+++
# CRUD
-  **C**reate
-  **R**ead
-  **U**pdate
-  **D**elete

Note:
The major functions needed for manipulating data in persistent storage (i.e. a database/webapp)

+++
# BREAD
-  **B**rowse
-  **R**ead
-  **E**dit
-  **A**dd
-  **D**elete

+++
# CRAP
-  **C**reate
-  **R**etrieve
-  **A**lter
-  **P**urge
<br/>
<img src="assets/tshirt.jpg" alt='Nice shirt' style='width: 200px;' />

+++
These actions map to an HTTP Method:
- **CREATE** = *POST*
- **READ** = *GET*
- **UPDATE** = *PUT*
- **DELETE** = *DELETE*

---
# Requests
- Specify the **method** (GET, POST, etc)
- URL
- url-encoded query string parameters ( `?meat=pork` )

+++
# Requests
- Headers include data about the request
	- Accept tells the server how you would like the response body represented
	- Can include auth tokens or authentication information
- May include "form data", like for creating or updating objects, or providing auth

+++
# Responses
- Headers include data about the response
	- Should the client cache this response?
	- What is the Content-Type of the response?
	- How is the text encoded?
+++
# Responses
- Response body
	- The requested representation
	- The results of an update or creation (id? full representation?)
- Status Code...

+++
# Status codes
