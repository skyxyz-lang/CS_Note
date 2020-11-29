#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 704.py
@time: 2020/11/29 13:32
@source: https://leetcode-cn.com/problems/binary-search/
@desc: 二分查找
"""


class Solution(object):
    """

    """
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (right - left) / 2 + left
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
        return -1
