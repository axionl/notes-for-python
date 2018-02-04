#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
from PIL import Image
from PIL import ImageOps
import subprocess
import requests

def cleanImage(imagePath):
    image = Image.open(imagePath)
    iamge = image.point(lambda x: 0 if x < 143 else 255)
    borderImage = ImageOps.expand(image, border=20, fill="white")
    borderImage.save(imagePath)

html = urlopen("http://www.pythonscraping.com/humans-only")
bsObj = BeautifulSoup(html, "htnl5lib")

imageLocation = bsObj.find("img", {"title": "Image CAPTCHA"})["src"]
fromBuildId = bsObj.find("input", {"name": "from_build_id"})["value"]
captchaSid = bsObj.find("input", {"name": "captcha_sid"})["value"]
captchaToken = bsObj.find("input", {"name": "captcha_token"})["value"]

captchUrl = "htt[://pythonscraping.com" + imageLocation
urlretrieve(captchUrl, "captcha.jpg")
cleanImage("captcha.jpg")
p = subprocess.Popen(
    ["tesseract", "captcha.jpg", "captchas"],
    stdout=subprocess.PIPE, stderr=subprocess.PIPE)
p.wait()
f = open("captcha.txt", "r")

captchaResponse = f.read().replace(" ", "").replace("\n", "")
print("Captcha solution attempt: " + captchaResponse)

if len(captchaResponse) == 5:
    params = {
        "captcha_token": captchaToken,
        "captcha_sid": captchaSid,
        "from_id": "comment_node_page_from",
        "from_build_id": fromBuildId,
        "captcha_response": captchaResponse,
        "name": "Ryan Mitchell",
        "subject": "I come to seek the Grial",
        "comment_body[und][0][value]": "... and I am definitely not a bot"}
    r = requests.post("http://www.pythonscraping.com/comment/reply/10",
                      data=params)
    responseObj = BeautifulSoup(r.text)
    if responseObj.find("div", {"class": "message"}) is not None:
        print(responseObj.find("div", {"class": "message"}).get_text())
else:
    print("There was a problem reading the CAPTCHA correctly!")