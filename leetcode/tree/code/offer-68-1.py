#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: offer-68-1.py
@time: 2020/11/21 11:19
@desc:剑指 Offer 68 - I. 二叉搜索树的最近公共祖先
@source: https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-zui-jin-gong-gong-zu-xian-lcof/
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
        if root == p or root == q:
            return root
        left = None
        right = None
        if p.val >= root.val and q.val >= root.val:
            right = self.lowestCommonAncestor(root.right, p, q)
        elif p.val <= root.val and q.val <= root.val:
            left = self.lowestCommonAncestor(root.left, p, q)
        else:
            return root
        if right:
            return right
        if left:
            return left
        return None
