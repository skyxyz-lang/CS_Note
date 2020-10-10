#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 1602.py
@time: 2020/10/10 16:08
@desc:
"""


class WordsFrequency(object):

    def __init__(self, book):
        """
        :type book: List[str]
        """
        self.book_count = {}
        for key in book:
            v = self.book_count.get(key, 0)
            v = v + 1
            self.book_count[key] = v

    def get(self, word):
        """
        :type word: str
        :rtype: int
        """
        return self.book_count.get(word, 0)


