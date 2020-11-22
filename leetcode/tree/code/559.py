#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 559.py
@time: 2020/11/21 10:58
@desc:  N叉树的最大深度
@source: https://leetcode-cn.com/problems/maximum-depth-of-n-ary-tree/
"""
from n_tree_node import Node


class Solution(object):
    """

    """
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
        depth_lst = []
        if not root:
            return 0
        for ch in root.children:
            depth_lst.append(self.maxDepth(ch))
        depth = 1
        if depth_lst:
            depth += max(depth_lst)
        return depth
