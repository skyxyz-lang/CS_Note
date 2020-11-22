#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 938.py
@time: 2020/11/21 00:05
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
        self.flag_end = False
        self.sum_val = 0

    def rangeSumBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: int
        """
        self.travel(root, low, high)
        return self.sum_val

    def travel(self, root, low, high):
        """

        :param root:
        :return:
        """
        if not root:
            return
        self.travel(root.left, low, high)
        val = root.val
        if high >= val >= low and not self.flag_end:
            self.sum_val += val
        elif val > high:
            self.flag_end = True
        self.travel(root.right, low, high)
