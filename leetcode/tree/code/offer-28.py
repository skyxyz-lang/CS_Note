#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: offer-28.py
@time: 2020/11/21 21:06
@source: https://leetcode-cn.com/problems/dui-cheng-de-er-cha-shu-lcof/
@desc: 对称的二叉树
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        res = self.compare(root.left, root.right)
        return res

    def compare(self, left, right):
        """

        :param left:
        :param right:
        :return:
        """
        if not left and not right:
            return True
        if left and right:
            return left.val == right.val and self.compare(left.left, right.right) and self.compare(left.right, right.left)
        else:
            return False
