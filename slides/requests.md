# Pragmatics: Making Basic Requests
- http://sal.awesome.com/api/machines/C0DEADBEEF01
- Method: GET
- Auth: Private key / Public key pair obtained through Sal UI
+++
# curl
```shell
$ curl \
	-H "privatekey:PRIVATEKEY" \
	-H "publickey:PUBLICKEY" \
	http://sal.awesome.com/api/machines/C0DEADBEEF01
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
# *301 Redirected*
+++
# curl
## Follow redirects with `--location`
```shell
$ curl \
	--location \
	-H "privatekey:PRIVATEKEY" \
	-H "publickey:PUBLICKEY" \
	http://sal.awesome.com/api/machines/C0DEADBEEF01
```

+++
## almost...
```
{"id":737,"serial":"C02SWZ3VGTF1","hostname":"mla806","operating_system":"10.12.5","memory":"16 GB","memory_kb":16777216,"munki_version":"3.0.0.3333","manifest":"C02SWZ3VGTF1","hd_space":"412775584","hd_total":"975831040","hd_percent":"58","console_user":"shcrai","machine_model":"MacBookPro13,3","machine_model_friendly":"MacBook Pro (15-inch, 2016)","cpu_type":"Intel Core i7","cpu_speed":"2.7 GHz","os_family":"Darwin","last_checkin":"2017-06-28T16:51:40.952013Z","first_checkin":"2017-01-05T20:08:09.464435Z","errors":0,"warnings":3,"activity":null,"puppet_version":"4.10.4","sal_version":"2.0.4","last_puppet_run":"2017-06-28T16:26:40Z","puppet_errors":0,"deployed":true,"machine_group":184}
```
+++
## Pretty print by piping to Python
```shell
$ curl \
	--location \
	-H "privatekey:PRIVATEKEY" \
	-H "publickey:PUBLICKEY" http://sal.awesome.com/api/machines/C0DEADBEEF01 \
	| python3 -m json.tool
```
+++
```
{
    "id": 737,
    "serial": "C0DEADBEEF01",
    "hostname": "tacomaster",
    "operating_system": "10.14.5",
    "memory": "256 GB",
    "memory_kb": 16777216,
    "munki_version": "3.0.0.3333",
    "hd_space": "256Tb",
    "hd_percent": "58",
    "console_user": "shcrai",
    "machine_model": "MacBookPro13,3",
    "machine_model_friendly": "MacBook Pro (15-inch, 2016)",
    "cpu_type": "Intel Core i7",
    "cpu_speed": "9.7 GHz",
    "os_family": "Darwin",
    "last_checkin": "2017-06-28T16:51:40.952013Z",
    "first_checkin": "2017-01-05T20:08:09.464435Z",
    "errors": 0,
    "warnings": 3,
    "activity": null,
    "puppet_version": "4.10.4",
    "sal_version": "2.0.4",
    "last_puppet_run": "2017-06-28T16:26:40Z",
    "puppet_errors": 0,
    "deployed": true,
    "machine_group": 184
}
```

+++
# httpie
```shell
$ brew install httpie
```
```shell
$ http --follow \
	http://sal.na.sas.com/api/machines/C02SWZ3VGTF1 \
	"privatekey:PRIVATEKEY" \
	"publickey:PUBLICKEY"
```
Note:
- GET method is implicit; simply specify a different method if you need it.
- Headers and form data are just optional arguments

+++?image=assets/httpie_sal.png&size=contain

Note:
Color styling is done by httpie; not because I'm showing it with highlight.js

+++
```shell
$ http -a USERNAME \
	POST \
	https://api.github.com/repos/jakubroztocil/httpie/issues/83/comments \
	body='HTTPie is awesome! :heart:'
```
+++
# Python 
## urllib from the interpreter
```
>>> import ssl
>>> import urllib.request
>>> request = urllib.request.Request('http://sal.na.sas.com/api/machines/C02SWZ3VGTF1')
>>> request.headers['privatekey'] = "PRIVATEKEY"
>>> request.headers['publickey'] = "PUBLICKEY"
>>> ctx = ssl.create_default_context()
>>> ctx.check_hostname = False
>>> ctx.verify_mode = ssl.CERT_NONE
>>> response = urllib.request.urlopen(request, context=ctx)
```
+++
# Requests
+++
# Curl -> Requests tool
+++
# Selenium / PhantomJS / Chromedriver for solving niggling problems.
Note:

Todo- what do you do about SSL?
Todo- auth types
TODO switch to using requests-oauthlib (oauth2, plugs into requests)
