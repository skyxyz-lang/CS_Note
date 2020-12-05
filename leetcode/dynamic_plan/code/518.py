#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 518.py
@time: 2020/12/3 23:30
@source: https://leetcode-cn.com/problems/coin-change-2/
@desc: 518. 零钱兑换 II
"""


class Solution(object):
    """

    """
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        m = len(coins) + 1
        n = amount + 1
        dp = [[0 for i in range(n)] for j in range(m)]
        for k in range(m):
            dp[k][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if j - coins[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j - coins[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[m-1][n-1]


if __name__ == '__main__':
    obj = Solution()
    print obj.change(5, [1, 2, 5])



