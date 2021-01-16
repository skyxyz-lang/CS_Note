#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 10.py
@time: 2021/1/16 21:26
@source: https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/
@desc: 剑指 Offer 10- I. 斐波那契数列 + 爬楼梯 非递归
"""


class Solution(object):

    def __init__(self):
        self.dic = {}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        f_n1 = 0
        f_n2 = 1
        if n < 2:
            return 1
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        f_n1 = 1
        f_n2 = 2
        for i in range(n-2):
            fn = f_n1 + f_n2
            print fn
            f_n2 = f_n1
            f_n1 = fn
        return f_n1 % 1000000007

    def fib1(self, n):
        """

        :param n:
        :return:
        """
        if n in self.dic:
            return self.dic[n]
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        else:
            k = self.fib1(n-1) + self.fib1(n-2)
            self.dic[n] = k
            return k


if __name__ == '__main__':
    obj = Solution()
    print obj.fib1(45)
