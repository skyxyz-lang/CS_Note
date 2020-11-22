#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 606.py
@time: 2020/11/22 09:40
@source:https://leetcode-cn.com/problems/construct-string-from-binary-tree/
@desc:606. 根据二叉树创建字符串
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""
        if not t.left and not t.right:
            return str(t.val)
        elif not t.right:
            return str(t.val) + "(" + self.tree2str(t.left) + ")"
        return str(t.val) + "(" + self.tree2str(t.left) + ")" + "(" + self.tree2str(t.right) + ")"
