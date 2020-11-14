#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: low_ances.py
@time: 2020/11/14 22:16
@desc:
"""


class TreeNode(object):
    """
    二叉树的节点定义以及中序遍历
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        root = self.dfs(root, p, q)
        return root

    def dfs(self, root, p, q):
        """

        :param root:
        :param p:
        :param q:
        :return:
        """
        if not root:
            return None
        if root.val == p.val or root.val == q.val:
            return root
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        if not left and not right:
            return None
        if left and right:
            return root
        if left:
            return left
        if right:
            return right


