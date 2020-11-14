#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: level.py
@time: 2020/11/14 10:52
@desc:
"""
class TreeNode(object):
    """
    二叉树的节点定义以及中序遍历
    """

    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """

    """

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        queue = []
        result = []
        queue.append(root)
        while len(queue) > 0:
            temp_val = []
            temp_queue = []
            while len(queue) > 0:
                root = queue.pop(0)
                temp_val.append(root.val)
                if root.left:
                    temp_queue.append(root.left)
                if root.right:
                    temp_queue.append(root.right)
            result.append(temp_val)
            queue = temp_queue
        return result

    def levelOrder2(self, root):
        """

        :param root:
        :return:
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
        return result
