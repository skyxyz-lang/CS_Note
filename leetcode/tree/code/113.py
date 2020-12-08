#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 113.py
@time: 2020/12/8 10:14
@source: https://leetcode-cn.com/problems/path-sum-ii/
@desc: 113. 路径总和 II
"""
from tree_node import TreeNode
from copy import deepcopy


class Solution(object):
    """

    """
    def __init__(self):
        self.final_result = []

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        self.travel(root, sum, [])
        return self.final_result

    def travel(self, root, sum_val, cur_path):
        """

        :param root:
        :param sum:
        :param cur_path:
        :return:
        """
        if not root:
            return
        if not root.left and not root.right:
            cur_path.append(root.val)
            if sum_val == sum(cur_path):
                self.final_result.append(deepcopy(cur_path))
            cur_path.pop()
            return
        cur_path.append(root.val)
        self.travel(root.left, sum_val, cur_path)
        self.travel(root.right, sum_val, cur_path)
        cur_path.pop()
