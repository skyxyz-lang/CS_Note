#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 104.py
@time: 2021/1/23 19:36
@source: https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/
@desc: 104. 二叉树的最大深度
"""
# 思路，递归，递归三要素，函数定义：求最大深度 出口：root == null 时候深度为0 ，递归等价关系：dep(root) = max(dep(root.left), dep(root.left)) + 1


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
