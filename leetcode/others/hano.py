#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: hano.py
@time: 2020/12/8 09:36
@source: https://leetcode-cn.com/problems/hanota-lcci/
@desc: 面试题 08.06. 汉诺塔问题
"""
# 递归的方式思考问题不应该看成自己调用自己，而是看成另外一个函数调用
# 递归解决问题的思路 1、递归函数的含义 2、问题拆分成子问题 3、问题的出口在哪里
# 1、把 n-1 个 盘子从A通过C移动到B，A剩余的盘子移动到C，B上面的盘子通过A移动到C


class Solution(object):
    """

    """
    def hanota(self, A, B, C):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :rtype: None Do not return anything, modify C in-place instead.
        """
        self.move(len(A), A, B, C)

    def move(self, n, A, B, C):
        """

        :param n:
        :param A: List[int]
        :param B: List[int]
        :param C: List[int]
        :return:
        """
        if n == 1:
            C.append(A.pop())
            return
        self.move(n-1, A, C, B)
        C.append(A.pop())
        self.move(n-1, B, A, C)

