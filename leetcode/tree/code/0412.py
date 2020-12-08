#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 0412.py
@time: 2020/12/8 10:35
@source: https://leetcode-cn.com/problems/paths-with-sum-lcci/
@desc: 面试题 04.12. 求和路径
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.result = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.travel(root, sum, [])
        return self.result

    def travel(self, root, sum_val, cur_path):
        if not root:
            return 0
        # 在遍历过程中，遍历每个路径
        cur_path.append(root.val)
        cur_sum = sum(cur_path)
        if cur_sum == sum_val:
            self.result += 1
        for i in range(len(cur_path)-1):
            cur_sum = cur_sum - cur_path[i]
            if cur_sum == sum_val:
                self.result += 1
        self.travel(root.left, sum_val, cur_path)
        self.travel(root.right, sum_val, cur_path)
        cur_path.pop()


