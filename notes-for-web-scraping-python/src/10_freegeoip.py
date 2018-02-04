#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from urllib.request import urlopen

def getCountry(ipAddress):
    respone = urlopen("http://freegeoip.net/json/" + ipAddress).read()
    responeJson = json.loads(respone)
    print(responeJson)
    return responeJson.get("country_code")

print(getCountry("50.78.253.58"))
