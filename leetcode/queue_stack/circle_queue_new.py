#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: circle_queue_new.py
@time: 2020/11/15 16:48
@desc:
"""


class MyCircularQueue(object):

    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self._lst = [0] * k
        self.cap = k
        self.length = k
        self.head = -1
        self.tail = -1

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.cap <= 0:
            return False
        if self.head == -1 and self.tail == -1:
            self.head = 0
            self.tail = 0
        else:
            self.tail = (self.tail + 1) % self.length
        self.cap -= 1
        self._lst[self.tail] = value
        return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.cap == self.length:
            return False
        else:
            self.head = (self.head + 1) % self.length
            self.cap += 1
            if self.cap == self.length:
                self.head = -1
                self.tail = -1
        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.head == -1:
            return -1
        return self._lst[self.head]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.tail == -1:
            return -1
        return self._lst[self.tail]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.cap == self.length:
            return True
        else:
            return False

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        if self.cap == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    circularQueue = MyCircularQueue(6)
    print circularQueue.enQueue(6)
    print circularQueue.Rear()
    print circularQueue.Rear()
    print circularQueue.deQueue()
    print circularQueue.enQueue(5)
    print circularQueue.Rear()
    print circularQueue.deQueue()
    print circularQueue.Front()
    print circularQueue.deQueue()
    print circularQueue.deQueue()
    print circularQueue.deQueue()
