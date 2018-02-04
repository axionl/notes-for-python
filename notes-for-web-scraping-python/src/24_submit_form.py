#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
<form method="post" action="processing.php">
First Name: <input type="text" name="firstname"><br>
Last Name: <input type="text" name="lastname"><br>
<input type="submit" value="Submit">
</form>
"""

import requests

params = {'firstname': "Ryan", 'lastname': 'Mitchell'}

r = requests.post("http://pythonscraping.com/files/processing.php", data=params)
print(r.text)

params = {'email_addr': 'ryan.e.mitchell@gmail.com'}
r = requests.post(
    "http://post.oreilly.com/client/o/oreilly/forms/quicksignup.cgi",
    data=params)
print(r.text)
