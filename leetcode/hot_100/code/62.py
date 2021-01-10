#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 62.py
@time: 2020/12/30 22:40
@source:  https://leetcode-cn.com/problems/unique-paths/
@desc: 62. 不同路径
"""
# 动态规划，初始状态 0 -- m 分别为0 - m， 0-n 也分别为 0-n，其中 dp[i][j]为到第i j 位置的走法 dp[i][j] = dp[i-1][j] + dp[i][j-1]


class Solution(object):
    """

    """
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(n):
            dp[0][i] = 1
        for i in range(m):
            dp[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if i - 1 >= 0:
                    dp[i][j] += dp[i-1][j]
                if j - 1 >= 0:
                    dp[i][j] += dp[i][j-1]
        return dp[m-1][n-1]


if __name__ == '__main__':
    obj = Solution()
    print obj.uniquePaths(3, 7)
