#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

# need proxy
textPage = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1.txt")
print(textPage.read())

textPage2 = urlopen("http://www.pythonscraping.com/pages/warandpeace/chapter1-ru.txt")
print(str(textPage2.read(), 'utf-8'))

html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
bsObj = BeautifulSoup(html, 'html5lib')
content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
content = bytes(content, "UTF-8")
content = content.decode("UTF-8")
