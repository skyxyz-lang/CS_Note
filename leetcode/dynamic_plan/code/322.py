#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 322.py
@time: 2020/12/3 22:58
@source: https://leetcode-cn.com/problems/coin-change/
@desc: 322. 零钱兑换
"""


class Solution(object):
    """

    """
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        memo = dict()
        def dp(n):
            """

            :param n:
            :return:
            """
            if n in memo:
                return memo[n]
            if n == 0:
                return 0
            elif n < 0:
                return -1
            res = float('inf')
            for coin in coins:
                sub_res = dp(n-coin)
                if sub_res == -1:
                    continue
                res = min(sub_res + 1, res)
            if res == float('inf'):
                res = -1
            memo[n] = res
            return res
        return dp(amount)

    def coinChange1(self, coins, amount):
        """

        :param coins:
        :param amount:
        :return:
        """
        dp = [(amount + 1) for i in range(amount + 1)]
        dp[0] = 0
        for i in range(0, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i - coin] + 1, dp[i])
        return dp[amount] if dp[amount] != (amount + 1) else -1
