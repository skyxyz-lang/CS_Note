#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: low_hight_tree.py
@time: 2020/11/20 23:26
@desc:https://leetcode-cn.com/problems/minimum-height-tree-lcci/
最小高度
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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        root = self.build(nums, 0, len(nums) -1)
        return root

    def build(self, nums, left, right):
        """

        :param nums:
        :param left:
        :param right:
        :return:
        """
        if left > right:
            return None
        mid = (right + left) / 2
        root = TreeNode(nums[mid])
        root.left = self.build(nums, left, mid - 1)
        root.right = self.build(nums, mid + 1, right)
        return root
