#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 720.py
@time: 2020/12/5 20:24
@source: https://leetcode-cn.com/problems/longest-word-in-dictionary/
@desc: 720. 词典中最长的单词
"""
# trie 字典树在单词查找中比较快速，常用来判断某个单词在不在一堆单词序列之中
# 字典树分为 建树 insert 以及 查找 search 的过程
# 字典树从根节点开始建树


class TrieNode(object):
    def __init__(self):
        self.is_end = False
        self.neighbor = {}


class Trie(object):
    """

    """
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        trie树单词插入
        :param word:
        :return:
        """
        cur = self.root
        for w in word:
            if w not in cur.neighbor:
                cur.neighbor[w] = TrieNode()
            cur = cur.neighbor[w]
        cur.is_end = True

    def search(self, word):
        """
        trie树单词查找
        :param word:
        :return:
        """
        cur = self.root
        for w in word:
            # 改造查找的过程，保证可以查询到数据
            if w not in cur.neighbor or not cur.neighbor[w].is_end:
                return False
            cur = cur.neighbor[w]
        return cur.is_end


class Solution(object):
    """

    """
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        trie = Trie()
        target_word = ""
        for word in words:
            trie.insert(word)
        for word in words:
            if trie.search(word):
                if len(word) > len(target_word):
                    target_word = word
                elif len(word) == len(target_word) and word < target_word:
                    target_word = word
        return target_word


