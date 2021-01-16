#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 7.py
@time: 2021/1/16 20:23
@source: https://leetcode-cn.com/problems/zhong-jian-er-cha-shu-lcof/
@desc: 剑指 Offer 07. 重建二叉树
"""
from tree_node import TreeNode


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not inorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        mid = inorder.index(root_val)
        root.left = self.buildTree(preorder[1: mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root
