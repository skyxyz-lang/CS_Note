#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: depth.py
@time: 2020/11/14 15:26
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