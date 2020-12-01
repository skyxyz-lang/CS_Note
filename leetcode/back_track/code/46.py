#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 46.py
@time: 2020/12/1 22:55
@source: https://leetcode-cn.com/problems/permutations/
@desc: 46. 全排列
"""
from copy import deepcopy


class Solution(object):
    """

    """
    def __init__(self):
        self.final_result = []

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.back_track(nums, [])
        return self.final_result

    def back_track(self, num, cur_path):
        """

        :param num:
        :param cur_path: List[int]
        :return:
        """
        if len(cur_path) == len(num):
            self.final_result.append(deepcopy(cur_path))
        for i in range(len(num)):
            if num[i] in cur_path:
                continue
            cur_path.append(num[i])
            self.back_track(num, cur_path)
            cur_path.pop()


if __name__ == '__main__':
    obj = Solution()
    print obj.permute([1, 2, 3])

