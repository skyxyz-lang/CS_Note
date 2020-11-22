#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 543.py
@time: 2020/11/22 11:29
@source:https://leetcode-cn.com/problems/diameter-of-binary-tree/
@desc:二叉树的直径
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.max_diameter = 0

    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.travel(root)
        return self.max_diameter

    def travel(self, root):
        """
        求而查处该节点左右子树的最大路径长度
        :param root:
        :return:
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        left = self.travel(root.left)
        right = self.travel(root.right)
        if (left + right) > self.max_diameter:
            self.max_diameter = left + right
        return max(left, right) + 1
