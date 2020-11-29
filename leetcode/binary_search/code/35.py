#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 35.py
@time: 2020/11/29 17:34
@source: https://leetcode-cn.com/problems/search-insert-position/
@desc: 35. 搜索插入位置
"""


class Solution(object):
    """

    """
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right)/2
            if nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid - 1
        if left >= len(nums):
            return 0
        return left
