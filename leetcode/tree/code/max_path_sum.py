#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: max_path_sum.py
@time: 2020/11/20 22:53
@desc:https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/
最大路径和
"""
import sys


class Solution(object):
    """

    """
    def __init__(self):
        self.max_sum = -sys.maxint-1

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root)
        return self.max_sum

    def dfs(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return 0
        left = max(0, self.dfs(root.left))
        right = max(0, self.dfs(root.right))
        num = root.val + left + right
        self.max_sum = max(self.max_sum, num)
        return root.val + max(left, right)
