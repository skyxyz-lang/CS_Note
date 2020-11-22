#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 111.py
@time: 2020/11/21 18:42
@source:
@desc:
"""
from tree_node import TreeNode
import sys


class Solution(object):
    """

    """
    def __init__(self):
        """

        """
        self.min_level = sys.maxint

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        self.travel(root, 0)
        return self.min_level

    def travel(self, root, depth):
        """

        :param root:
        :param depth:
        :return:
        """
        if not root:
            return
        if not root.left and not root.right:
            self.min_level = min(depth + 1, self.min_level)
        self.travel(root.left, depth + 1)
        self.travel(root.right, depth + 1)
