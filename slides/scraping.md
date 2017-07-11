# Web-scraping

- lxml.html (works just like etree)
	- But can handle broken HTML
		- Of which there is a *lot*
- BeautifulSoup4
	- Extremely navigable
	- Different API from ElementTree / lxml
	- With html5lib can create valid HTML
- Scrapy
	- Async framework for data mining by crawling

+++?image=assets/sda_nes_games.png&size=contain

+++?code=examples/beautiful_soup/nes.py
@[6-8]
@[12-13]
@[14-16]
@[17-18]

+++?image=assets/nes.png&size=contain
+++?image=assets/bad_dudes.png&size=contain
+++?code=examples/beautiful_soup/nes2.py
@[8]
@[17-19]
+++?image=assets/nes2.png&size=contain

+++
# Selenium
## safaridriver, chromedriver, geckodriver and PhantomJS
