#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 3.py
@time: 2021/1/16 16:35
@source:https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/
@desc: 剑指 Offer 03. 数组中重复的数字
"""


class Solution(object):

    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for n in nums:
            if n in dic:
                return n
            else:
                dic[n] = 1
        return -1
