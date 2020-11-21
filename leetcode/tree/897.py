#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 897.py
@time: 2020/11/21 10:19
@desc:递增顺序查找树
@source:https://leetcode-cn.com/problems/increasing-order-search-tree/
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.val = []

    def increasingBST(self, root):
        """
        先遍历后建树
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return root
        self.travel(root)
        root = self.build(self.val, 0)
        return root

    def travel(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return
        self.travel(root.left)
        self.val.append(root.val)
        self.travel(root.right)

    def build(self, nums, index):
        """

        :param nums:
        :param index:
        :return:
        """
        if len(nums) - 1 < index:
            return None
        root = TreeNode(nums[index])
        root.right = self.build(nums, index + 1)
        return root
