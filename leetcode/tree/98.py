#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 98.py
@time: 2020/11/20 23:08
@desc: 验证二叉搜索树
https://leetcode-cn.com/problems/validate-binary-search-tree/
"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys


class Solution(object):

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        st = []
        node = root
        pre_val = - sys.maxint - 1
        while len(st) > 0 or node:
            if node:
                st.append(node)
                node = node.left
            else:
                if len(st) > 0:
                    node = st.pop()
                    if node.val <= pre_val:
                        return False
                    pre_val = node.val
                    node = node.right
        return True
