#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 108.py
@time: 2020/11/21 09:34
@desc:https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/
将有序数组转换为二叉搜索树
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
        root = self.build(nums, 0, len(nums) - 1)
        return root

    def build(self, nums, low, high):
        """

        :param nums:
        :param low:
        :param high:
        :return:
        """
        if low > high:
            return None
        mid = (low + high) / 2
        val = nums[mid]
        root = TreeNode(val)
        root.left = self.build(nums, low, mid-1)
        root.right = self.build(nums, mid + 1, high)
        return root
