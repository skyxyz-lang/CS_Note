#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 122.py
@time: 2020/12/5 17:16
@source: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
@desc: 122. 买卖股票的最佳时机 II
"""


class Solution(object):
    """

    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        dp = [[0 for i in range(2)] for j in range(len(prices))]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, len(prices)):
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])
            dp[i][1] = max(dp[i-1][1], dp[i-1][0] - prices[i])
        return dp[len(prices) - 1][0]