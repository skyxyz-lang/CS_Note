#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 78.py
@time: 2020/12/1 22:30
@source: https://leetcode-cn.com/problems/subsets/
@desc: 78. 子集
"""
from copy import deepcopy


class Solution(object):
    """

    """
    def __init__(self):
        self.final_result = []

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.back_track(nums, 0, [])
        return self.final_result

    def back_track(self, nums, start, cur_res):
        """

        :param nums:
        :param start:
        :param cur_res:
        :return:
        """
        self.final_result.append(deepcopy(cur_res))
        for i in range(start, len(nums)):
            cur_res.append(nums[i])
            self.back_track(nums, i + 1, cur_res)
            cur_res.pop()


if __name__ == '__main__':
    obj = Solution()
    print obj.subsets([1, 2, 3])
