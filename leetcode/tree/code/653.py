#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 653.py
@time: 2020/11/21 23:10
@source:https://leetcode-cn.com/problems/two-sum-iv-input-is-a-bst/
@desc: 两数之和 IV - 输入 BST
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.travel_val = {}
        self.res = False

    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        self.travel(root, k)
        return self.res

    def travel(self, root, target):
        """

        :param root:
        :param target:
        :return:
        """
        if not root:
            return
        self.travel(root.left, target)
        val = target - root.val
        if val in self.travel_val:
            self.res = True
            return
        else:
            self.travel_val[root.val] = 1
        self.travel(root.right, target)
