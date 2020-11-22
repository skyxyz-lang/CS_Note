#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: offer-55-2.py
@time: 2020/11/21 18:52
@source:https://leetcode-cn.com/problems/ping-heng-er-cha-shu-lcof/
@desc:  平衡二叉树
"""
from tree_node import TreeNode
import math


class Solution(object):
    """

    """
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        left = self.depth(root.left)
        right = self.depth(root.right)
        return math.fabs(left-right) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def depth(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return 0
        left = self.depth(root.left)
        right = self.depth(root.right)
        return max(left, right) + 1
