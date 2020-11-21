#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 404.py
@time: 2020/11/21 22:57
@source: https://leetcode-cn.com/problems/sum-of-left-leaves/
@desc: 左叶子之和
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.lst = []

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.travel(root, None)
        return sum(self.lst)

    def travel(self, node, parent):
        """

        :param node:
        :param parent:
        :return:
        """
        if node:
            if parent:
                if not node.right and not node.left and parent.left == node:
                    self.lst.append(node.val)
            self.travel(node.left, node)
            self.travel(node.right, node)

