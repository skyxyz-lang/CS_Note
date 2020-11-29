#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 567.py
@time: 2020/11/29 21:57
@source: https://leetcode-cn.com/problems/permutation-in-string/
@desc: 567. 字符串的排列
"""


class Solution(object):
    """

    """
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        need = dict()
        windows = dict()
        left = 0
        right = 0
        valid = 0
        for c in s1:
            self.add_dict_one(c, need)
        while right < len(s2):
            c = s2[right]
            right += 1
            self.add_dict_one(c, windows)
            if windows.get(c, 0) == need.get(c, -1):
                valid += 1
            while (right - left) >= len(s1):
                d = s2[left]
                left += 1
                if valid == len(need):
                    return True
                if windows.get(d, 0) == need.get(d, -1):
                    valid -= 1
                self.reduce_dict_one(d, windows)
        return False

    def add_dict_one(self, key, dic):
        """

        :param key:
        :param dic:
        :return:
        """
        if key in dic:
            dic[key] = dic[key] + 1
        else:
            dic[key] = 1

    def reduce_dict_one(self, key, dic):
        """

        :param key:
        :param dic:
        :return:
        """
        if key in dic:
            dic[key] = dic[key] - 1