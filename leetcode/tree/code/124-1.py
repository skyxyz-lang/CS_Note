#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 124-1.py
@time: 2020/12/8 11:33
@source:https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
@desc:124. 二叉树中的最大路径和
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.max_path = float('-inf')

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.maxGain(root)
        return self.max_path

    def maxGain(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return 0
        left = max(self.maxGain(root.left), 0)
        right = max(self.maxGain(root.right), 0)
        self.max_path = max(root.val + +left + right, self.max_path)
        return root.val + max(left, right)
