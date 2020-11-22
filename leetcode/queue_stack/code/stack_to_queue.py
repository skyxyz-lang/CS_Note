#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: stack_to_queue.py
@time: 2020/11/19 23:29
@desc: 栈实现队列
https://leetcode-cn.com/leetbook/read/queue-stack/gvtxe/
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st1 = []
        self.st2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.st1.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        if self.st2:
            return self.st2.pop()
        return -1

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        if self.st2:
            return self.st2[-1]
        return -1

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.st2 and not self.st1:
            return True
        else:
            return False


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(10)
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
