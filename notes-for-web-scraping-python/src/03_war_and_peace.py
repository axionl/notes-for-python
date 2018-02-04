#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTitle(url):
    """Get the title of pages."""
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as err:
        print(err)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html5lib")
    except AttributeError as err:
        print(err)
        return None
    else:
        title = bsObj.body.h1
        return title

def get_text(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as err:
        print(err)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html5lib")
    except AttributeError as err:
        print(err)
        return None
    else:
        nameList = bsObj.find_all("span", {"class":{"green", "red"}})
        return nameList

url = "http://www.pythonscraping.com/pages/warandpeace.html"

title = getTitle(url)
if title == None:
    print("Title could not be found")
else:
    print(title.get_text())

nameList = get_text(url)
if nameList == None:
    print("Text cloud not be found")
else:
    for name in nameList:
        print(name.get_text())