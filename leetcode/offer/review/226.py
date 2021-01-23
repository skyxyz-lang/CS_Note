#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 226.py
@time: 2021/1/23 17:32
@source: https://leetcode-cn.com/problems/invert-binary-tree/
@desc: 226. 翻转二叉树
"""
# 思路，二叉树问题一般想到递归，反转是，在根之下，左右调换，并且递归调换
from tree_node import TreeNode


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        left = self.invertTree(root.left)
        right = self.invertTree(root.right)
        root.right = left
        root.left = right
        return root



