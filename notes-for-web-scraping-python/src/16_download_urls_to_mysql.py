#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
import MySQLdb

conn = MySQLdb.connect('localhost', 'root', 'dianzi313+', 'wikipedia')
cur = conn.cursor()
pages = set()

# def creatTable(cur, conn):
#     cur.execute("USE wikipedia")
#     cur.execute('''CREATE TABLE 'wikipedia'.'pages' (
#         `id` INT NOT NULL AUTO_INCREMENT,
#         `url` VARCHAR(255) NOT NULL,
#         `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#         PRIMARY KEY(`id`));''')
#     cur.execute('''CREATE TABLE 'wikipedia'.'links' (
#         `id` INT NOT NULL AUTO_INCREMENT,
#         `fromPageId` INT NULL,
#         `toPageId` INT NULL,
#         `created` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#         PRIMARY KEY(`id`));''')
#     conn.commit()
#     conn.close()

def insertPageIfNotExists(url):
    cur.execute("SELECT * FROM pages WHERE url = %s", (url))  # TODO: Fix this format bug.
    if cur.rowcount == 0:
        cur.execute("INSERT INTO pages (url) VALUES (\"%s\")", (url))
        conn.commit()
        return cur.lastrowid
    else:
        return cur.fetchone()[0]

def insertLink(fromPageId, toPageId):
    cur.execute("SELECT * FROM links WHERE fromPageId = %s AND toPageId = %s", (int(fromPageId), int(toPageId)))
    if cur.rowcount == 0:
        cur.execute("INSERT INTO links (fromPageId, toPageId) VALUES (\"%s\", \"%s\")", (int(fromPageId), int(toPageId)))
        conn.commit()

def getLinks(pageUrl, recursionLevel):
    global pages
    if recursionLevel > 4:
        return;
    pageId = insertPageIfNotExists(pageUrl)
    html = urlopen("http://en.wikipedia.org" + pageUrl)
    bsObj = BeautifulSoup(html, "html5lib")
    for link in bsObj.findAll("a", href=re.compile("^(/wiki/)((?!:).)*$")):
        insertLink(pageId, insertPageIfNotExists(link.attrs["href"]))
        if link.attrs["href"] not in pages:
            newPage = link.attrs["href"]
            pages.add(newPage)
            getLinks(newPage, recursionLevel+1)

try:
    pass
    # _ = creatTable(cur)
except IOError:
    print("DATABASE has been created.")
finally:
    getLinks("/wiki/Kevin_Bacon", 0)
    cur.close()
    conn.close()
