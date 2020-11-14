#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 535.py
@time: 2020/10/10 15:24
@desc:
"""


class Codec:

    def __init__(self):
        self.pool = {}

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        short = longUrl[-10]
        self.pool[short] = longUrl
        return short

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.pool[shortUrl]