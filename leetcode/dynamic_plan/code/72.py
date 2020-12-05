#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 72.py
@time: 2020/12/5 17:36
@source: https://leetcode-cn.com/problems/edit-distance/
@desc: 72. 编辑距离
"""


class Solution(object):
    """

    """
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(n+1):a
            dp[0][i] = i
        for j in range(m+1):
            dp[j][0] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i][j-1]+1, dp[i-1][j] + 1, dp[i-1][j-1] + 1)
        return dp[m][n]
