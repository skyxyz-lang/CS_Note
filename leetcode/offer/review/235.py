#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 235.py
@time: 2021/1/23 18:23
@source: https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
@desc: 235. 二叉搜索树的最近公共祖先
"""
# 思路：二叉树的公共最先
from tree_node import TreeNode


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
