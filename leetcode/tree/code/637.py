#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 637.py
@time: 2020/11/21 11:31
@desc:637. 二叉树的层平均值
@source: https://leetcode-cn.com/problems/average-of-levels-in-binary-tree/
"""
from tree_node import TreeNode
import collections


class Solution(object):
    """

    """
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        lst = []
        queue = collections.deque([root])
        while len(queue) > 0:
            sum_val = 0
            cur_len = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                sum_val += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            lst.append(sum_val / (1.0*cur_len))
        return lst
