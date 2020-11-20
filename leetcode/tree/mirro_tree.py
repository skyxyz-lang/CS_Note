#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: sym_tree.py
@time: 2020/11/20 23:41
@desc: 二叉树的镜像
https://leetcode-cn.com/classic/problems/er-cha-shu-de-jing-xiang-lcof/description/
"""


class TreeNode(object):
    """
    二叉树的节点定义以及中序遍历
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """

    """
    def mirrorTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return None
        root.left, root.right = self.mirrorTree(root.right), self.mirrorTree(root.left)
        return root
