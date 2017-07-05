# Google Image Search for Python
## Introduction

## Configuration
1. Visit https://cse.google.com/ and add a Custom Search Engine.
	a. Leave the `Sites to Search` field blank to search the entire web.
	b. Enter a name for the search engine (mandatory).
	c. In the `Advanced Options` section, enter `ImageObject` as a schema type.
	d. Hit the `Create` button.
	e. Toggle the `Image Search` slider on the edit page for the new CSE.
	f. Under the `Details` section, click on the `Search Engine ID` to get the
	`CX` value needed to use this search engine in python.
2. Visit https://code.google.com/apis/console and create a new project.
	a. While on the new project's page, select the `Enable APIs and get
	credentials like keys` button.
	b. Click on the `Credentials` menu item on the lefthand side.
	c. Click on `Create a Credential`, then `API Key` to create key for your
	project. This is the `key` value needed by the python class.
3. Enable the `Custom Search API`
	a. While still on the console page for your new project, find the `Custom
	Search API` link and click it.
	b. Click the `enable` button.
