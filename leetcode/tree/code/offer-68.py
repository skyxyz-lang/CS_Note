#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: offer-68.py
@time: 2020/11/21 11:05
@desc: 二叉树的最近公共祖先
@source: https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        if right:
            return right
        if left:
            return left
        return None
