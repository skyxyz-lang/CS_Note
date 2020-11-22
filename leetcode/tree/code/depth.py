#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: depth.py
@time: 2020/11/14 15:26
@desc:
"""


class TreeNode(object):
    """
    二叉树的节点定义以及中序遍历
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """

    """
    def __init__(self):
        self.ans = 0

    def maxDepth(self, root):
        """
        自底向上获得结果
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        return max(left, right) + 1

    def max_depth_new(self, root, depth):
        """
        自顶向下，遍历过程中全局记录
        :param root:
        :param depth:
        :return:
        """
        if not root:
            return
        if not root.left and not root.right:
            self.ans = max(self.ans, depth)
        self.max_depth_new(root.left, depth+1)
        self.max_depth_new(root.right, depth+1)
