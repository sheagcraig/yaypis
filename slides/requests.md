# Pragmatics: Making Basic Requests
- http://sal.awesome.com/api/machines/C0DEADBEEF01
- Method: GET
- Auth: Private key / Public key pair obtained through Sal UI
+++
# curl
```shell
$ curl -H "privatekey:PRIVATEKEY" -H "publickey:PUBLICKEY" http://sal.awesome.com/api/machines/C0DEADBEEF01
```
+++
## wha...?
```
<html>
	<head>
		<title>301 Moved Permanently</title>
	</head>
	<body bgcolor="white">
		<center><h1>301 Moved Permanently</h1></center>
		<hr><center>nginx/1.11.4</center>
	</body>
</html>
```

Note:
Didn't discuss status code 301, it means you got redirected, in this case by a proxy.
+++?image=assets/etcake.jpg&size=contain
# 301 Redirected
+++
# curl
## Follow redirects with `--location`
```shell
$ curl --location -H "privatekey:PRIVATEKEY" -H "publickey:PUBLICKEY" http://sal.awesome.com/api/machines/C0DEADBEEF01
```
+++
# httpie
+++
# Getting curl args from Chrome dev panel
+++
# Python +++
# urllib from the interpreter
+++
# requests
+++
# Curl -> Requests tool
+++
# Selenium / PhantomJS / Chromedriver for solving niggling problems.
Note:

Todo- what do you do about SSL?
Todo- auth types
