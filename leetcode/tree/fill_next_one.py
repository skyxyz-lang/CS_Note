#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: fill_next_one.py
@time: 2020/11/14 21:38
@desc:
"""


class TreeNode1(object):
    """
    二叉树的节点定义
    """

    def __init__(self, val=0, left=None, right=None, next=None):
        """

        :param val:
        :param left:
        :param right:
        :param next:
        """
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        queue = [root]
        while len(queue) > 0:
            queue_size = len(queue)
            cur = queue.pop(0)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)
            if queue_size > 1:
                for i in range(0, queue_size -1):
                    next = queue.pop(0)
                    if next.left:
                        queue.append(next.left)
                    if next.right:
                        queue.append(next.right)
                    cur.next = next
                    cur = next
                next.next = None
        return root



