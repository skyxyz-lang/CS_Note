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

    def coinChange2(self, coins, amount):
        """

        :param coins:
        :param amount:
        :return:
        """
        m = len(coins)
        n = amount
        dp = [[0 for i in range(n+1)] for j in range(m+1)]
        for i in range(n+1):
            dp[0][i] = amount + 1
        dp[0][0] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                if j - coins[i-1] >= 0:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-coins[i-1]] + 1)
                else:
                    dp[i][j] = dp[i-1][j]
        return -1 if dp[m][n] == (amount+1) else dp[m][n]


if __name__ == '__main__':
    obj = Solution()
    print obj.coinChange2([1, 2, 5], 5)
