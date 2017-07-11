# Create a REST API for existing services
+++
# loopback
http://loopback.io

+++?image=assets/loopback-screens/1lb-init.png&size=contain
Note: 
Initializing loopback application...

+++?image=assets/loopback-screens/2lb-db.png&size=contain
Note:
Adding MongoDB datasource (to be connected with model)

+++?image=assets/loopback-screens/3lb-model.png&size=contain
Note:
Creating model for tacos, linking to mongo datasource, and adding properties

+++?image=assets/loopback-screens/4lb-node.png&size=contain
Note: 
Starting node server

+++?image=assets/loopback-screens/5lb-explorer.png&size=contain
Note: 
Explorer view - lists all API endpoints and allows you to test them

+++?image=assets/loopback-screens/6lb-post.png&size=contain
Note: 
Creating a POST request

+++?image=assets/loopback-screens/7lb-response.png&size=contain
Note: 
POST request 200 response

+++
# APIStar
https://github.com/tomchristie/apistar

+++
```shell
apistar new . --layout minimal
```

+++?code=examples/apistar/app.py
@[3-5]
@[45-49]
@[23-25]
@[15-20]

+++
```shell
apistar run
```
+++?code=slides/apistar_interpreter.py
@[1-2]
@[3-4]
@[4207-4218]
@[4280-4288]
@[4289-4290]
@[4340-4351]

+++?image=assets/apistar_docs.png&size=contain
+++?image=assets/apistar_interact.png&size=contain

+++
# Flask
## Munki client manifest service

+++?code=examples/client_manifest_flask/client_manifest_flask.py
@[49-51]
@[63-65]
@[67-69]
@[76]
@[96-98]
@[115]

+++
## Django Options
- http://tastypieapi.org
- http://www.django-rest-framework.org
