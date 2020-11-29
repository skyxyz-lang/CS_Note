#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 222.py
@time: 2020/11/29 15:50
@source:https://leetcode-cn.com/problems/count-complete-tree-nodes/
@desc: 222. 完全二叉树的节点个数
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1
