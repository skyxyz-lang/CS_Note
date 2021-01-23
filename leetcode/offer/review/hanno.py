#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: hanno.py
@time: 2021/1/23 15:06
@source: https://leetcode-cn.com/problems/hanota-lcci/
@desc: 面试题 08.06. 汉诺塔问题
"""


# 思路
# 1、汉诺塔问题主要是通过B，把A的盘子移到C上
# 当A只有一个盘子的时候，直接A移到C，当有多个的时候，先把n-1个移动到B，把剩下的一个移动到C，再把N-1个移动到C


class Solution(object):
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
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :return:
        """
        if n == 1:
            C.append(A.pop())
            return
        self.move(n-1, A, C, B)
        C.append(A.pop())
        self.move(n-1, B, A, C)


if __name__ == '__main__':
    obj = Solution()
    B = []
    C = []
    obj.hanota([1, 2, 3, 4, 5], B, C)
    print C
