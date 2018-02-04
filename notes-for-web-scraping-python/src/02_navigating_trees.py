#!/usr/bin/python3
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "http://www.pythonscraping.com/pages/page3.html"
html = urlopen(url)
bsObj = BeautifulSoup(html.read(), "html5lib")

for child in bsObj.find("table", {"id": "giftList"}).children:
    print(child)
    print("------------------------------------------")

print("-====================================-")

for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    print(sibling)
    print("------------------------------------------")

print("-====================================-")

print(bsObj.find("img", {"src": "../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())

