#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: circle_queue.py
@time: 2020/11/15 16:01
@desc:
"""


class MyCircularQueue(object):
    """
    不借助容量，借助容量实现应该简单点
    """

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self._lst = [0] * k
        self.length = k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.head == -1 and self.tail == -1:
            self.head = 0
            self.tail = 0
        else:
            tail = (self.tail + 1) % self.length
            if tail == self.head:
                return False
            self.tail = tail
        self._lst[self.tail] = value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.head == self.tail and self.head != -1:
            self.head = -1
            self.tail = -1
            return True
        elif self.head == self.tail and self.head == -1:
            return False
        else:
            self.head = (self.head + 1) % self.length
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.head == -1:
            return -1
        else:
            return self._lst[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.tail == -1:
            return -1
        else:
            return self._lst[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.tail == -1 and self.head == -1:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        tail_next = (self.tail + 1) % self.length
        if tail_next == self.head:
            return True
        else:
            return False


if __name__ == '__main__':
    circularQueue = MyCircularQueue(3)
    print circularQueue.enQueue(1)
    print circularQueue.enQueue(2)
    print circularQueue.enQueue(3)
    print circularQueue.enQueue(4)
    print circularQueue.Rear()
    print circularQueue.isFull()
    print circularQueue.deQueue()
    print circularQueue.enQueue(4)
    print circularQueue.Rear()
