#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 100.py
@time: 2021/1/23 18:19
@source: https://leetcode-cn.com/problems/same-tree/
@desc: 100. 相同的树
"""
# 思路和对称二叉树类似，都是比较左右节点，比较左右节点是否值相同，以及递归比较 时间复杂度为O(n)，空间复杂度为O(n)，调用栈的深度


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if not p and not q:
            return True
        elif p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return False
