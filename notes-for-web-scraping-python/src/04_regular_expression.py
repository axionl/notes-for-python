#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError
import re

def get_img_name(url):
    try:
        html = urlopen(url)
    except (HTTPError, URLError) as err:
        print(err)
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html5lib")
        imgs = bsObj.find_all("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
    except AttributeError as err:
        print(err)
        return None
    return imgs

url = "http://www.pythonscraping.com/pages/page3.html"
images = get_img_name(url)
for image in images:
    print(image["src"])