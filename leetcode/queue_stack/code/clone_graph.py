#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: clone_graph.py
@time: 2020/11/19 08:21
@desc:https://leetcode-cn.com/leetbook/read/queue-stack/gmcr6/
"""

# Definition for a Node.


class Node(object):
    """

    """
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    """

    """
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        if node in self.visited:
            return self.visited[node]
        new_node = Node(node.val, [])
        self.visited[node] = new_node
        for no in node.neighbors:
            new_node.neighbors.append(self.cloneGraph(no))
        return new_node
