#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 107.py
@time: 2020/11/21 17:36
@source:https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/
@desc: 二叉树的层次遍历 II
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = [root]
        result = []
        while len(queue) > 0:
            temp_val = []
            for i in range(len(queue)):
                root = queue.pop(0)
                temp_val.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
            result.append(temp_val)
        result.reverse()
        return result
