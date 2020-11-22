#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 700.py
@time: 2020/11/21 00:19
@desc:
"""


class TreeNode(object):
    """
    二叉树的节点定义
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """

    """
    def __init__(self):
        self.target = None

    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return self.target
        if root.val == val:
            self.target = root
        elif root.val > val:
            self.searchBST(root.left, val)
        else:
            self.searchBST(root.right, val)
        return self.target
