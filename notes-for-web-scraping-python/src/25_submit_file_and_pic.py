#!/usr/bin/env python
# -*- coding: utf-8 -*-

# <form action="processing2.php" method="post" enctype="multipart/form-data">
#     Submit a jpg, png, or gif: <input type="file" name="uploadFile"><br>
#     <input type="submit" value="Upload File">
# </form>

import requests

files = {'uploadFile': open('../files/Python-logo.png', 'rb')}
r = requests.post("http://pythonscraping.com/paes/processing2.php", files=files)
print(r.text)
