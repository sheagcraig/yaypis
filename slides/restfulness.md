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
- The data exchanged is representational, meaning it may be in multiple formats that do not
  resemble the native storage (e.g. XML or JSON vs. a SQL table row).
- Resources could be anything; files, concepts, (computers in your management tool, status updates on twitter)
- The REST API abstracts the storage of resources from the interface for getting at them.
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
## What does it mean *practically* to consume **REST?**

+++?image=assets/request_flowchart.jpg&size=contain

+++
## Request are **made** by the *client*
- *URL* determines resource on which to operate.
- *HTTP method* determines action to take.
- *Headers* configure things like auth, requested return type.
- *Form data* passes app data.

+++
## Responses are **returned** by the *server*
- *Satus codes* indicate the result
- *Body* includes the requested data or details about the results
- *Headers* describe the response

+++
## *URL* determines resource on which to operate
- Resources are mapped to a collection of URLs 
	- API base
		- https://tacos.jk/api
		- Resources:
			- */cat_videos*
			- */dog_videos*
			- */crawly_thing_videos*
+++
## Resources may have different endpoints for different purposes
- Collection
	- */cat_videos*
- Individual
	- */cat_videos/452440293*
- Query strings
	- */cat_videos?type=adorable*

+++
## What do we want to *DO* with a resource?
## CRUD
-  **C**reate
-  **R**ead
-  **U**pdate
-  **D**elete

Note:
The major functions needed for manipulating data in persistent storage (i.e. a database/webapp)

+++
## BREAD
-  **B**rowse
-  **R**ead
-  **E**dit
-  **A**dd
-  **D**elete

+++
## CRAP
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

+++
## Headers configure the request
- *Accept* **application/json**
- Auth info

## Data to be sent is serialized
- It's all bytes

+++
# Responses
## Status Codes
- Numeric code indicates result of request
- First digit specifies class of response
- **1xx** *Informational*
- **2xx** *Success*
- **3xx** *Redirection*
- **4xx** *Client Error*
- **5xx** *Server Error*

+++
## Status Codes: Most Common
## *200*   **400**  *404*
## **201**   *401*  **409**
## *204*   **403**  *500*

+++?image=assets/status_codes.jpg&size=contain
# The Nicolas Cage Status Code Mnemonic
+++?image=assets/200.jpg&size=contain
# 200 **OK**
+++?image=assets/201.jpg&size=contain
# 201 **Created**
+++?image=assets/204.jpg&size=contain
# 204 **No Content**

Note:
No Content is really saying "we've accepted your request, but the server doesn't need to return anything; don't update your view"
i.e. an UPDATE happened, and you already have the data.

+++?image=assets/400.jpg&size=contain
# 400 **Bad Request** 
+++?image=assets/401.png&size=contain
# 401 **Unauthorized**

Note:
Authentication hasn't happened, you're authenticating wrong.

+++?image=assets/403.jpg&size=contain
# 403 **Forbidden**
(You shall not pass)

Note:
Authentication has happened, but you don't have rights.
+++?image=assets/404.png&size=contain
# 404 **Not Found**
+++?image=assets/409.jpg&size=contain
# 409 **Conflict**
+++?image=assets/500.png&size=contain
# 500 **Internal Server Error** 

+++

## Response Body is Serialized
- Body is in bytes
- Can be deserialized into XML, JSON

## Response Headers
- Headers include data about the response
	- Should the client cache this response?
	- What is the Content-Type of the response?
	- How is the text encoded?
