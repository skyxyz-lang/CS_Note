#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: min_st.py
@time: 2020/11/16 23:26
@desc: 最小栈问题：https://leetcode-cn.com/leetbook/read/queue-stack/g5l7d/
思考，不适用额外的栈
"""
import sys


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_st = [sys.maxsize]
        self.data_st = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data_st.append(x)
        self.min_st.append(min(self.min_st[-1], x))

    def pop(self):
        """
        :rtype: None
        """
        self.data_st.pop()
        self.min_st.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.data_st[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_st[-1]


if __name__ == '__main__':
    obj = MinStack()
    obj.push(0)
    obj.push(1)
    obj.push(0)
    print obj.min_value
    print obj.min_st
    print obj.data_st
    print obj.getMin()
    obj.pop()
    print obj.min_value
    print obj.min_st
    print obj.data_st
    print obj.top()
    print obj.getMin()


