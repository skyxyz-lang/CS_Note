#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 501.py
@time: 2020/11/22 09:58
@source: https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/
@desc: 二叉搜索树中的众数
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.pre_val = None
        self.result = []
        self.max_times = 0
        self.cur_times = 0

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.travel(root)
        return self.result

    def travel(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return
        self.travel(root.left)
        if self.pre_val is None:
            self.result = [root.val]
            self.max_times = 1
            self.cur_times = 1
        else:
            if root.val == self.pre_val:
                self.cur_times += 1
            else:
                self.cur_times = 1
            if self.cur_times > self.max_times:
                self.result = [root.val]
                self.max_times = self.cur_times
            elif self.cur_times == self.max_times:
                self.result.append(root.val)
        self.pre_val = root.val
        self.travel(root.right)
