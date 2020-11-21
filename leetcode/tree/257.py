#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 257.py
@time: 2020/11/21 18:22
@source:https://leetcode-cn.com/problems/binary-tree-paths/
@desc: 二叉树的所有路径
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        """

        """
        self.path_lst = []

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        self.travel(root, "")
        return self.path_lst

    def travel(self, root, path):
        """

        :param root:
        :param path:
        :return:
        """
        if not root:
            return
        if not root.left and not root.right:
            if path:
                path += "->" + str(root.val)
            else:
                path = str(root.val)
            self.path_lst.append(path)
            return
        if path:
            path += "->" + str(root.val)
        else:
            path = str(root.val)
        self.travel(root.left, path)
        self.travel(root.right, path)
