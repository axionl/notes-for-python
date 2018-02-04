#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from urllib.request import urlopen
import time


def sendMail(subject, body):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg["Form"] = "christmas_alerts@pythonscraping.com"
    msg['To'] = "axionl@aosc.io"


s = smtplib.SMTP('localhost')
s.send_message(msg)
s.quit()

bsObj = BeautifulSoup(urlopen("https://isitchristmas.com"))
while(bsObj.find("a", {"id": "answer"}).attrs["title"] == "NO"):
    print("It is not Christmas yet.")
    time.sleep(3600)
sendMail("It's Christmas!",
         "According to https://isitchristmas.com, it is Christmas")
