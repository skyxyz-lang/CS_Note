#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 965.py
@time: 2020/11/21 17:28
@source:https://leetcode-cn.com/problems/univalued-binary-tree/
@desc: 单值二叉树
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.res = {}

    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.dfs(root)
        if len(self.res) > 1:
            return False
        else:
            return TreeNode

    def dfs(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return
        self.dfs(root.left)
        self.res[root.val] = 1
        self.dfs(root.right)