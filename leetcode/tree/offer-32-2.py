#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: offer-32-2.py
@time: 2020/11/21 15:02
@desc:从上到下打印二叉树 II
@source:https://leetcode-cn.com/problems/cong-shang-dao-xia-da-yin-er-cha-shu-ii-lcof/
"""
from tree_node import TreeNode
import collections


class Solution(object):
    """

    """
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        if not root:
            return result
        queue = collections.deque([root])
        while len(queue) > 0:
            tmp = []
            for i in range(len(queue)):
                node = queue.popleft()
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(tmp)
        return result
