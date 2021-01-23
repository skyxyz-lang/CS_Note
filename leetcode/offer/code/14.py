#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 14.py
@time: 2021/1/17 16:40
@source: https://leetcode-cn.com/problems/jian-sheng-zi-lcof/
@desc: 剑指 Offer 14- I. 剪绳子
"""
# 思路1：数学法，对于求 y = (n/x)^x 最大值，可以证明当 x = e的时候取值最大，然而要求x是整数，所以为x=3的时候取值最大，对于小于3的
# n = 2 y = 1; n=3 y=2 n = 4 y = 4
# 思路二：自顶向下，递归法，拆分成子问题  cuttingRope(n) 代表 剪成m段，并且最大乘积，那么 cuttingRope(n) = max(j * (n - j) + j * cuttingRope(n-j))
# 在此基础之上，可以采用记忆化技术，减少计算量
# 思路三：可以采用自底向上的思路，这时候一般是使用动态规划，从小到大递推
# 用 dp[i] 表示长度为 n 的绳子，剪断后最大乘积  dp[i] = max(dp[i], j * (i-j) , j * dp[i-j])
# 分别表示 j段 i-j不剪  j段 i-j继续剪 整个不剪


class Solution(object):
    def __init__(self):
        self.memory = {}

    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2:
            return 1
        if n == 3:
            return 2
        if n == 4:
            return 4
        res = 1
        mod = 1000000007
        while n > 4:
            res = (res * 3) % mod
            n = n - 3
        return (res * n) % mod

    def cuttingRopeRec(self, n):
        """

        :param n:
        :return:
        """
        if n < 4:
            return n - 1
        if n == 4:
            return 4
        res = -1
        for i in range(n):
            res = max(res, max(i * (n-i), i * self.cuttingRopeRec(n - i)))
        return res

    def cuttingRopeRecWithMemory(self, n):
        """
        从顶向下，记忆化搜索
        :param n:
        :return:
        """
        if n in self.memory:
            return self.memory[n]
        if n < 4:
            return n - 1
        if n == 4:
            return 4
        res = -1
        for i in range(1, n):
            res = max(res, max(i * (n-i), i * self.cuttingRopeRecWithMemory(n - i)))
        self.memory[n] = res
        return self.memory[n]

    def cuttingRope1(self, n):
        """

        :param n:
        :return:
        """
        if n < 4:
            return n - 1
        dp = [0 for i in range(n+1)]
        dp[2] = 1
        dp[3] = 2
        for i in range(n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], j*(i-j), j*dp[i-j])
        return dp[n]
