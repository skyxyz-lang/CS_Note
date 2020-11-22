#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: tree_node.py
@time: 2020/11/21 09:49
@desc:
"""


class TreeNode(object):
    """
    二叉树的节点定义
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
