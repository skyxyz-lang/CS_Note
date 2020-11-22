#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 590.py
@time: 2020/11/21 00:14
@desc: N叉树后续遍历
https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal/
"""


class Node(object):
    """

    """
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution(object):
    """

    """
    def __init__(self):
        self.res = []

    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if not root:
            return self.res
        for ch in root.children:
            self.postorder(ch)
        self.res.append(root.val)
        return self.res
