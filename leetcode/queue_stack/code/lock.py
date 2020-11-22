#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: lock.py
@time: 2020/11/15 21:22
@desc:
"""
import collections


class Solution(object):
    """
    打开转盘锁， 看成一张图进行搜索
    """
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        dead_ends = set(deadends)
        used = {"0000"}
        if "0000" in dead_ends:
            return -1
        queue = collections.deque([("0000", 0)])
        while len(queue) > 0:
            (node, depth) = queue.popleft()
            if node == target:
                return depth
            if node in dead_ends:
                continue
            neighbours = self.neighbour(node)
            for n in neighbours:
                if n not in used:
                    used.add(n)
                    queue.append((n, depth+1))
        return -1

    def neighbour(self, node):
        """
        寻找邻居
        :param node:
        :return:
        """
        for i in range(4):
            for j in (1, -1):
                y = (int(node[i]) + j) % 10
                yield node[:i] + str(y) + node[i+1:]
