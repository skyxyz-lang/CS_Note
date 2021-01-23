#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 15.py
@time: 2021/1/17 18:33
@source: https://leetcode-cn.com/problems/er-jin-zhi-zhong-1de-ge-shu-lcof/
@desc: 剑指 Offer 15. 二进制中1的个数
"""
# 思路：移位以及位运算


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        num = 0
        for i in range(32):
            if n & 1 == 1:
                num += 1
            n = n >> 1
        return num
