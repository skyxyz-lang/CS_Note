#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 993.py
@time: 2020/11/21 21:31
@source:https://leetcode-cn.com/problems/cousins-in-binary-tree/
@desc:二叉树的堂兄弟节点
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        """

        """
        self.dep_map = {}
        self.par_map = {}

    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        self.travel(root, None)
        return self.dep_map.get(x) == self.dep_map.get(y) and self.par_map.get(x) != self.par_map.get(y)

    def travel(self, node, parent):
        """

        :param node:
        :param parent:
        :return:
        """
        if node:
            if not parent:
                self.dep_map[node.val] = 0
            else:
                self.dep_map[node.val] = self.dep_map[parent.val] + 1
                self.par_map[node.val] = parent.val
            self.travel(node.left, node)
            self.travel(node.right, node)