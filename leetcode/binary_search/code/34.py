#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 34.py
@time: 2020/11/29 15:39
@source: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/
@desc: 34. 在排序数组中查找元素的第一个和最后一个位置
"""


class Solution(object):
    """

    """
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        return [self.search_left_bound(nums, target), self.search_right_bound(nums, target)]

    def search_left_bound(self, nums, target):
        """
        寻找左边界
        :param nums:
        :param target:
        :return:
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

        if left >= len(nums) or nums[left] != target:
            return -1
        return left

    def search_right_bound(self, nums, target):
        """
        寻找右边界
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
                left = mid + 1
        if right < 0 or nums[right] != target:
            return -1
        return right
