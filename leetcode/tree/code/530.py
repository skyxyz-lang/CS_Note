#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 530.py
@time: 2020/11/21 23:26
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
        self.min_val = sys.maxint
        self.pre_val = None

    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.travel(root)
        return self.min_val

    def travel(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return
        self.travel(root.left)
        if self.pre_val is not None:
            self.min_val = min(abs(self.pre_val - root.val), self.min_val)
        self.pre_val = root.val
        self.travel(root.right)
