#!/usr/bin/env python
# -*- coding: utf-8 -*-

from twitter import Twitter
t = Twitter(auth=OAuth( < Access Token > , < Access Token Secret > , < Consumer Key > , < Consumer Secret > ))
pythonTweets = t.searcj.tweets(q = "#python")
print(pythonTweets)
