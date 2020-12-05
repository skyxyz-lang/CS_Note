#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 1143.py
@time: 2020/12/5 18:12
@source: https://leetcode-cn.com/problems/longest-common-subsequence/
@desc: 1143. 最长公共子序列
"""


class Solution(object):
    """

    """
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        m = len(text1)
        n = len(text2)
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        # base case
        for i in range(1, m+1):
            for j in range(1, n+1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        return dp[m][n]
