#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 31.py
@time: 2020/12/19 22:47
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
        if len(nums) < 2:
            return nums
        index = len(nums) - 2
        while index >= 0:
            if nums[index] >= nums[index+1]:
                index -= 1
            else:
                break
        if index < 0:
            self.reverse(nums, 0, len(nums) -1)
        else:
            tail = len(nums) - 1
            while nums[tail] <= nums[index]:
                tail -= 1
            tmp = nums[index]
            nums[index] = nums[tail]
            nums[tail] = tmp
            self.reverse(nums, index+1, len(nums) -1)

    def reverse(self, num, i, j):
        """

        :param num:
        :param i:
        :param j:
        :return:
        """
        while i < j:
            num[i], num[j] = num[j], num[i]
            i += 1
            j -= 1


if __name__ == '__main__':
    obj = Solution()
    num = [3, 2, 1, 4]
    obj.nextPermutation(num)
    print num
