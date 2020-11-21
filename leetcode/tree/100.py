#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 100.py
@time: 2020/11/21 22:03
@source: https://leetcode-cn.com/problems/same-tree/
@desc: 相同的树
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def isSameTree(self, p, q):
        """
        和对称二叉树有异曲同工之处
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q:
            if p.val != q.val:
                return False
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False
