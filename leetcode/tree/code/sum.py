#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: sum.py
@time: 2020/11/14 16:39
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
    def __init__(self):
        self.result = False

    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        self.dfs(root, 0, sum)
        return self.result

    def dfs(self, root, path_sum, sum):
        """

        :param root:
        :param path_sum:
        :param sum:
        :return:
        """
        if not root:
            return
        if not root.left and not root.right:
            path_sum = path_sum + root.val
            if path_sum == sum:
                self.result = True
        self.dfs(root.left, path_sum+root.val, sum)
        self.dfs(root.right, path_sum + root.val, sum)
