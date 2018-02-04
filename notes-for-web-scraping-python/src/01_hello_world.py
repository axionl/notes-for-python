#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup

def getTtiel(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as err:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html5lib")
        title = bsObj.body.h1
    except AttributeError as err:
        return None
    return title

title = getTtiel("http://www.jianshu.com/p/805590e7cd09")
if title == None:
    print("Title could not be found")
else:
    print(title)
