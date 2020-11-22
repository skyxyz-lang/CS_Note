#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 671.py
@time: 2020/11/22 10:44
@source:https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree/
@desc:671. 二叉树中第二小的节点
"""
from tree_node import TreeNode
import sys


class Solution(object):
    """

    """
    def __init__(self):
        self.min_value = sys.maxint

    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return -1
        self.dfs(root, root.val)
        if self.min_value == sys.maxint:
            return -1
        else:
            return self.min_value

    def dfs(self, root, target):
        """

        :param root:
        :param target:
        :return:
        """
        if not root:
            return
        if root.val > target:
            self.min_value = min(self.min_value, root.val)
        self.dfs(root.left, target)
        self.dfs(root.right, target)



