#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 54.py
@time: 2020/11/21 09:46
@desc:https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-di-kda-jie-dian-lcof/
二叉搜索树的第k大节点
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.index = 0
        self.val = []

    def kthLargest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.travel(root, k)
        return self.val[len(self.val) - k]

    def travel(self, root, k):
        """

        :param root:
        :param k:
        :return:
        """
        if not root:
            return None
        self.travel(root.left, k)
        self.val.append(root.val)
        self.travel(root.right, k)
