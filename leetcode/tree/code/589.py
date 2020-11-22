#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 589.py
@time: 2020/11/21 10:11
@desc:  N叉树的前序遍历
@source:https://leetcode-cn.com/problems/n-ary-tree-preorder-traversal/
"""
from n_tree_node import Node


class Solution(object):
    """

    """
    def __init__(self):
        self.val = []

    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        self.travel(root)
        return self.val

    def travel(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return
        self.val.append(root.val)
        for ch in root.children:
            self.travel(ch)




