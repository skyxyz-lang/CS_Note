#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 436.py
@time: 2020/11/29 16:06
@source: https://leetcode-cn.com/problems/find-right-interval/
@desc: 436. 寻找右区间
"""


class Solution(object):
    """

    """
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        maps = dict()
        lst = []
        index = 0
        res = []
        for interval in intervals:
            begin = interval[0]
            lst.append(begin)
            maps[begin] = index
            index += 1
        lst = sorted(lst)
        for interval in intervals:
            end = interval[1]
            target = self.left_bound(lst, end)
            if target >= len(lst):
                res.append(-1)
            else:
                res.append(maps.get(lst[target]))
        return res

    def left_bound(self, nums, target):
        """

        :param nums:
        :param target:
        :return:
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) / 2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid - 1
        return left
