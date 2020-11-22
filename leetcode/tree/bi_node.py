#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: bi_node.py
@time: 2020/11/22 11:53
@source:https://leetcode-cn.com/problems/binode-lcci/
@desc:面试题 17.12. BiNode
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.pre_node = TreeNode(-1)

    def convertBiNode(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        tmp = self.pre_node
        self.travel(root)
        return tmp.right

    def travel(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return None
        self.travel(root.left)
        self.pre_node.right = root
        self.pre_node = root
        root.left = None
        self.travel(root.right)