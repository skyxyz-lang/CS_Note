#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: lru.py
@time: 2020/11/16 22:42
@desc: 最近最少使用算法
"""


class DLinkedListNode(object):
    """
    定义双向链表
    """
    def __init__(self, k=0, v=0):
        self.key = k
        self.value = v
        self.ne_xt = None
        self.pre = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 0
        self.exist_map = {}
        self.head = DLinkedListNode()
        self.tail = DLinkedListNode()
        self.head.ne_xt = self.tail
        self.head.pre = None
        self.tail.pre = self.head
        self.tail.ne_xt = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.exist_map:
            return -1
        else:
            node = self.exist_map[key]
            self.remove_to_head(node)
            return node.value

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.exist_map:
            node = self.exist_map[key]
            node.value = value
            self.remove_to_head(node)
        else:
            if self.size >= self.capacity:
                node = self.remove_tail()
                self.exist_map.pop(node.key)
            else:
                self.size += 1
            node = DLinkedListNode(key, value)
            self.exist_map[key] = node
            self.add_to_head(node)

    def remove_tail(self):
        """

        :param node:
        :return:
        """
        node = self.tail.pre
        self.remove_node(node)
        return node

    def remove_to_head(self, node):
        """

        :param node: DLinkedListNode
        :return:
        """
        self.remove_node(node)
        self.add_to_head(node)

    def add_to_head(self, node):
        """

        :param node: DLinkedListNode
        :return:
        """
        node.ne_xt = self.head.ne_xt
        node.pre = self.head
        self.head.ne_xt.pre = node
        self.head.ne_xt = node

    def remove_node(self, node):
        """

        :param node: DLinkedListNode
        :return:
        """
        node.pre.ne_xt = node.ne_xt
        node.ne_xt.pre = node.pre
