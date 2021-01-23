#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 101.py
@time: 2021/1/23 17:45
@source: https://leetcode-cn.com/problems/symmetric-tree/
@desc: 101. 对称二叉树
"""
# 思路，二叉树的对称是根节点的左右子节点的叶子节点对称相等，有着 a.left == b.right and a.right == b.left
from tree_node import TreeNode


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        """

        :param left:
        :param right:
        :return:
        """
        if not left and not right:
            return True
        elif left and right:
            return left.val == right.val and self.compare(left.right, right.left) and self.compare(left.left, right.right)
        else:
            return False
