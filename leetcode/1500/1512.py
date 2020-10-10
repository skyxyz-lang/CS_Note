#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 1512.py
@time: 2020/10/10 14:49
@desc:
"""


class Solution(object):

    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        ans = 0
        for num in nums:
            if not dic.get(num):
                dic[num] = 1
            else:
                ans += dic[num]
                dic[num] = dic[num] + 1
        return ans
