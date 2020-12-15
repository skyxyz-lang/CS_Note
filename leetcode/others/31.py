#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 31.py
@time: 2020/12/12 21:19
@source: https://leetcode-cn.com/problems/next-permutation/
@desc: 31. 下一个排列
"""


class Solution(object):
    """

    """
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return nums
        length = len(nums)
        index = length - 2
        while index >= 0 and nums[index] >= nums[index+1]:
            index -= 1
        if index < 0:
            self.reverse(nums, 0, length-1)
        else:
            index_min = length - 1
            while index_min >= 0 and nums[index_min] <= nums[index]:
                index_min -= 1
            tmp = nums[index]
            nums[index] = nums[index_min]
            nums[index_min] = tmp
            self.reverse(nums, index+1, length-1)

    def reverse(self, nums, begin, end):
        """

        :param nums:
        :param begin:
        :param end:
        :return:
        """
        while begin < end:
            nums[begin], nums[end] = nums[end], nums[begin]
            begin += 1
            end -= 1


if __name__ == '__main__':
    obj = Solution()
    obj.nextPermutation([1, 3, 2])
    obj.nextPermutation([5, 1, 1])
    obj.nextPermutation([3, 2, 1])
