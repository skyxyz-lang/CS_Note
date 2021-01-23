#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: offer68-2.py
@time: 2021/1/23 18:39
@source: https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/
@desc: 剑指 Offer 68 - II. 二叉树的最近公共祖先
"""
# 思路：1、p、q的公共祖先指的p、q深度最大的祖先，首先满足是祖先，然后是深度最大，p q的祖先可以是自己
# lowestCommonAncestor 为找到root为根节点，p、q的公共祖先，当root == p or root == q,最近公共祖先即为root，
# 否则的话，在左右子树中分别寻找，如果左右子树都有公共节点,

from tree_node import TreeNode


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q:
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

