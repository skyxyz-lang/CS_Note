#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 94.py
@time: 2020/10/10 16:14
@desc:
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution(object):

    def __init__(self):
        self.res = []

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return self.res
        if root.left:
            self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)
        return self.res

    def inorderTraversal1(self, root):
        if not root:
            return self.res
        lst = []
        current = root
        while current:
            if current.left:
                lst.append(current.left)
                current = current.left





