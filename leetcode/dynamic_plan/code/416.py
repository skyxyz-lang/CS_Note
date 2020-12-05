#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 416.py
@time: 2020/12/5 15:29
@source: https://leetcode-cn.com/problems/partition-equal-subset-sum/
@desc: 416. 分割等和子集
"""


class Solution(object):
    """

    """
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        sum_all = sum(nums)
        if sum_all % 2 != 0:
            return False
        m = len(nums) + 1
        n = sum_all/2
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            dp[i][0] = True
        for j in range(n):
            dp[0][j] = False
        for i in range(1, m):
            for j in range(1, n):
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j - nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m-1][n-1]
