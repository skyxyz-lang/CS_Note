#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: build_mid_pre.py
@time: 2020/11/14 21:24
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


class Solution(object):
    """

    """
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        root = self.build(0, len(inorder) - 1, preorder, inorder)
        return root

    def build(self, left, right, preorder, inorder):
        """
        先序和中序遍历，先建立左子树
        :param left:
        :param right:
        :param preorder:
        :param inorder:
        :return:
        """
        if left > right:
            return
        root_val = preorder.pop(0)
        root = TreeNode(root_val)
        index = inorder.index(root_val)
        root.left = self.build(left, index - 1, preorder, inorder)
        root.right = self.build(index + 1, right, preorder, inorder)
        return root
