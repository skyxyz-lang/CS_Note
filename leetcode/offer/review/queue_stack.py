#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: queue_stack.py
@time: 2021/1/23 23:43
@source:
@desc:
"""
# 使用队列实现栈,栈的主要操作是 进栈和出栈，先进后出
# 主要依赖于两个队列
#  当入队的时，选择一个非空队列进行入队，再把另一个队列的值全部放到当前队列，这样就实现了后入的排在队首，先出


class Stack(object):
    """

    """
    def __init__(self):
        """

        """
        self.q1 = []
        self.q2 = []

    def push(self, val):
        """

        :param val:
        :return:
        """
        if not self.q1:
            self.q1.append(val)
            while not self.q2:
                self.q1.append(self.q2.pop(0))
        elif not self.q2:
            self.q2.append(val)
            while not self.q1:
                self.q2.append(self.q1.pop(0))

    def pop(self):
        """

        :return:
        """
        if not self.q1:
            self.q1.pop(0)
        elif not self.q2:
            self.q2.pop(0)
