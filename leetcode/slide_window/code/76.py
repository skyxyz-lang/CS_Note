#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 76.py
@time: 2020/11/29 21:15
@source: https://leetcode-cn.com/problems/minimum-window-substring/
@desc: 76. 最小覆盖子串
"""
"""
思路主要是滑动窗口
1、滑动窗口的区间是[left, right) 左闭右开
2、判断什么时候 右滑、什么时候左滑、什么时候更新结果
3、window 和 need 分别存储当前窗口的状态和需要的状态
"""
import sys


class Solution(object):
    """

    """
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        need = dict()
        windows = dict()
        for c in t:
            self.add_dict_one(c, need)
        left = 0
        right = 0
        valid = 0
        start = 0
        length = sys.maxint
        # 右边进行滑动
        while right < len(s):
            c = s[right]
            right += 1
            self.add_dict_one(c, windows)
            # 判断当前window 和 need 是否满足
            if windows.get(c, 0) == need.get(c, -1):
                valid += 1
            while valid == len(need):
                if (right - left) < length:
                    length = right - left
                    start = left
                d = s[left]
                left += 1
                if windows.get(d, 0) == need.get(d, -1):
                    valid -= 1
                self.reduce_dict_one(d, windows)
        res_str = ""
        print start
        print length
        if length != sys.maxint:
            res_str = s[start:start + length]
        return res_str

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
