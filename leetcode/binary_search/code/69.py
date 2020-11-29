#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 69.py
@time: 2020/11/29 15:55
@source: https://leetcode-cn.com/problems/sqrtx/
@desc: 69. x 的平方根
"""


class Solution(object):
    """

    """
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        left = 0
        right = x
        while left <= right:
            mid = (left + right)/2
            if mid * mid > x:
                right = mid -1
            elif mid * mid < x:
                left = mid + 1
            elif mid * mid == x:
                return mid
        return left - 1
