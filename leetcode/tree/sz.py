#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: sz.py
@time: 2020/11/14 22:31
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


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return "X"
        left = self.serialize(root.left)
        right = self.serialize(root.right)
        return str(root.val) + "," + left + "," + right

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data_lst = data.split(",")
        root = self.build_tree(data_lst)
        return root

    def build_tree(self, data_lst):
        """

        :param data_lst:
        :return:
        """
        root_val = data_lst.pop(0)
        if root_val == 'X':
            return None
        root = TreeNode(root_val)
        root.left = self.build_tree(data_lst)
        root.right = self.build_tree(data_lst)
        return root
