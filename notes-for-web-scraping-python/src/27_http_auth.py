#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from requests.auth import AuthBase
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('rayn', 'password')
r = requests.post(
    url="http://pythonscraping.com/pages/auth/login.php", auth=auth)
print(r.text)
