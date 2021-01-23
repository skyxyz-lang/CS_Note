#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: stack_queue.py
@time: 2021/1/23 23:44
@source:
@desc:
"""
# 使用栈实现队列，主要思路是双栈法
# 分为两个栈，一个为入栈，另一个作为出栈
# 每次数据放到入栈
# 每次出栈判断出栈数据是否为空，如果为空把入栈数据全部放到出栈，否则直接出栈即可


class Solution(object):
    """

    """
    def __init__(self):
        """

        """
        self.in_st = []
        self.out_st = []

    def push(self, val):
        """

        :param val:
        :return:
        """
        self.in_st.append(val)

    def pop(self):
        """

        :return:
        """
        if not self.out_st:
            self.out_st.pop()
        else:
            while not self.in_st:
                self.out_st.append(self.in_st.pop())
            self.out_st.pop()