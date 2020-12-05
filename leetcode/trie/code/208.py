#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 208.py
@time: 2020/12/5 20:54
@source:
@desc:
"""


class TrieNode(object):
    """

    """
    def __init__(self):
        self.is_end = False
        self.neighbor = {}


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for w in word:
            if w not in cur.neighbor:
                cur.neighbor[w] = TrieNode()
            cur = cur.neighbor[w]
        cur.is_end = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for w in word:
            if w not in cur.neighbor:
                return False
            cur = cur.neighbor[w]
        # 搜索结束，如果 is_end 为true即为找到，否则为找不到
        return cur.is_end

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for w in prefix:
            if w not in cur.neighbor:
                return False
            cur = cur.neighbor[w]
        # 搜索结束且未被打断，则是前缀，否则不是前缀，和search有所区别
        return True

