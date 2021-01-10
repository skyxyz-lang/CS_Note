#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 416.py
@time: 2021/1/3 20:10
@source: https://leetcode-cn.com/problems/hamming-distance/
@desc: 461. 汉明距离
"""
# 思路 先异或，再看每一位是不是1


class Solution(object):

    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        distance = 0
        xor = x ^ y
        while xor:
            if xor & 1 == 1:
                distance += 1
            xor = xor >> 1
        return distance


