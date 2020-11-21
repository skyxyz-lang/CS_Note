#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 669.py
@time: 2020/11/21 17:54
@source: https://leetcode-cn.com/problems/trim-a-binary-search-tree/
@desc: 修剪二叉搜索树
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.first = True
        self.first_high = True

    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """



