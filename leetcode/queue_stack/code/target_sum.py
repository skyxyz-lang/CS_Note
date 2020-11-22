#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: target_sum.py
@time: 2020/11/19 23:03
@desc:
https://leetcode-cn.com/leetbook/read/queue-stack/ga4o2/
以下解法DFS均超时
"""


class Solution(object):
    """

    """
    def __init__(self):
        self.count = 0

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        length = len(nums)
        self.dfs_new(nums, 0, 0, S, length)
        return self.count

    def dfs_new(self, nums, index, sum_num, target, length):
        """

        :param nums:
        :param index:
        :param sum_num:
        :param target:
        :return:
        """
        if index == length:
            if sum_num == target:
                self.count += 1
        else:
            self.dfs_new(nums, index+1, sum_num + nums[index], target, length)
            self.dfs_new(nums, index + 1, sum_num - nums[index], target, length)

    def dfs(self, nums, index, target):
        """

        :param nums:
        :param index:
        :param target:
        :return:
        """
        ans = 0
        if index == len(nums):
            return 0
        elif index == len(nums) - 1:
            if target == nums[index]:
                ans += 1
            if target == -nums[index]:
                ans += 1
            return ans
        up = self.dfs(nums, index+1, target - nums[index])
        down = self.dfs(nums, index+1, target + nums[index])
        return up + down


if __name__ == '__main__':
    obj = Solution()
    print obj.findTargetSumWays([11,31,37,36,43,40,50,18,10,15,10,35,43,25,41,43,6,22,38,38], 44)