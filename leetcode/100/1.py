#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 1.py
@time: 2020/10/10 11:35
@desc:
"""


class Solution(object):

    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
        dic = {}
        for i in xrange(len(nums)):
            dic[nums[i]] = i
        for j in xrange(len(nums)):
            v = target - nums[j]
            if v in dic and dic[v] != j:
                res = [j, dic[v]]
                break
        return res


if __name__ == '__main__':
    obj = Solution()
    print obj.twoSum([2, 7, 11, 15], 9)
