#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: sym.py
@time: 2020/11/14 15:47
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
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self.dfs(root.left, root.right)

    def dfs(self, left, right):
        """
        递归的方式
        :param left:
        :param right:
        :return:
        """
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return self.dfs(left.left, right.right) and self.dfs(left.right, right.left)

    def no_dfs(self, root):
        """
        非递归方式
        :param root:
        :return:
        """
        queue = []
        if not root:
            return True
        if not root.left and not root.right:
            return True
        if not root.left or not root.right:
            return False
        queue.append(root.left)
        queue.append(root.right)
        while len(queue) > 0:
            left = queue.pop(0)
            right = queue.pop(0)
            if not left and not right:
                continue
            if not left or not right:
                return False
            if left.val != right.val:
                return False
            queue.append(left.left)
            queue.append(right.right)
            queue.append(left.right)
            queue.append(right.left)
        return True
