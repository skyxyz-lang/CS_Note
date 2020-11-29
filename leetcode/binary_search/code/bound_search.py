#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: bound_search.py
@time: 2020/11/29 17:19
@source:
@desc:
"""


class Solution(object):
    """

    """
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

        if left >= len(nums):
            return -1
        return left

    def right_bound(self, nums, target):
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
                left = mid + 1
        if right < 0:
            return -1
        return right


if __name__ == '__main__':
    obj = Solution()
    #    0  1  2  3  4  5  6  7  8  9  10 11 12 13  14
    a = [1, 1, 1, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 10, 10]
    print obj.left_bound(a, 2)
    print obj.right_bound(a, 2)