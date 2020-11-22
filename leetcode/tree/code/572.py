#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 572.py
@time: 2020/11/22 10:23
@source: https://leetcode-cn.com/problems/subtree-of-another-tree/
@desc: 另一个树的子树
"""
from tree_node import TreeNode


class Solution(object):
    """

    """

    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        # 防止isSame比较空节点
        if not s:
            return False
        return self.isSamme(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

    def isSamme(self, t1, t2):
        """

        :param t1:
        :param t2:
        :return:
        """
        if not t1 and not t2:
            return True
        elif t1 and t2:
            if t1.val == t2.val and self.isSamme(t1.left, t2.left) and self.isSamme(t1.right, t2.right):
                return True
        return False
