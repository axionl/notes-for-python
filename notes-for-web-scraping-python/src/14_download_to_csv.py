#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
from urllib.request import urlopen
from bs4 import BeautifulSoup

def genCsv(path):
    with open(path, "w+") as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(('number', 'number plus 2', 'number times 2'))
        for i in range(10):
            writer.writerow((i, i + 2, i * 2))

path = "src/14_csvFile.csv"
_ = genCsv(path)

html = urlopen("http://en.wikipedia.org/wiki/Comparison_of_text_editors")
bsObj = BeautifulSoup(html, "html5lib")
table = bsObj.findAll("table", {"class": "wikitable"})[0]
rows = table.findAll("tr")


with open(path, 'w+') as csvFile:
    writer = csv.writer(csvFile)
    for row in rows:
        csvRow = []
        for cell in row.findAll(['td', 'th']):
            csvRow.append(cell.get_text())
        writer.writerow(csvRow)
