#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: queue_to_stack.py
@time: 2020/11/19 23:47
@desc: 栈实现队列
https://leetcode-cn.com/problems/implement-stack-using-queues/solution/
"""

import collections


class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.qu1 = collections.deque([])
        self.qu2 = collections.deque([])

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        if self.qu1:
            self.qu1.append(x)
            while self.qu2:
                self.qu1.append(self.qu2.popleft())
        elif self.qu2:
            self.qu2.append(x)
            while self.qu1:
                self.qu2.append(self.qu1.popleft())

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.qu2:
            return self.qu2.popleft()
        if self.qu1:
            return self.qu1.popleft()
        return -1

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if self.qu2:
            return self.qu2[0]
        if self.qu1:
            return self.qu1[0]
        return -1

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.qu2 and not self.qu1:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    obj.top()
    obj.pop()
    obj.empty()