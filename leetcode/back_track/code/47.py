#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 47.py
@time: 2020/12/1 23:41
@source: https://leetcode-cn.com/problems/permutations-ii/
@desc: 47. 全排列 II
"""
from copy import deepcopy


class Solution(object):
    """

    """
    def __init__(self):
        self.final_result = []

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        checked = [0 for i in range(len(nums))]
        self.back_track(nums, checked, [])
        return self.final_result

    def back_track(self, nums, checked, cur_path):
        """

        :param nums:
        :param checked:
        :param cur_path:
        :return:
        """
        if len(cur_path) == len(nums):
            print cur_path
            self.final_result.append(deepcopy(cur_path))
        for i in range(len(nums)):
            if checked[i] == 1:
                continue
            if i > 0 and nums[i] == nums[i-1] and checked[i-1] == 1:
                continue
            cur_path.append(nums[i])
            checked[i] = 1
            self.back_track(nums, checked, cur_path)
            cur_path.pop()
            checked[i] = 0


if __name__ == '__main__':
    obj = Solution()
    print obj.permuteUnique([1, 1, 2])
