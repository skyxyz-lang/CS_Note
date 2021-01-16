#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 5.py
@time: 2021/1/16 19:31
@source:https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/
@desc:剑指 Offer 05. 替换空格
"""


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s.replace(" ", "%20")
