#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 669.py
@time: 2020/11/21 17:54
@source: https://leetcode-cn.com/problems/trim-a-binary-search-tree/
@desc: 修剪二叉搜索树
"""
from tree_node import TreeNode


class Solution(object):
    """

    """

    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        if root.val > high:
            return self.trimBST(root.left, low, high)
        root.left = self.trimBST(root.left, low, high)
        root.right = self.trimBST(root.right, low, high)
        return root





