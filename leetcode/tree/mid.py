#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: mid.py
@time: 2020/11/14 10:23
@desc:
"""


class TreeNode(object):
    """
    二叉树的节点定义以及中序遍历
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """

    """
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        lst = []
        self.travel(root, lst)
        return lst

    def travel(self, root, lst):
        """

        :param root:
        :param lst:
        :return:
        """
        if not root:
            return
        self.travel(root.left, lst)
        lst.append(root.val)
        self.travel(root.right, lst)

    def in_order_no_dfs(self, root):
        """
        中序遍历非递归
        :param root:
        :return:
        """
        if not root:
            return []
        result = []
        st = []
        node = root
        while node or len(st) > 0:
            if node:
                st.append(node)
                node = node.left
            else:
                node = st.pop()
                result.append(node.val)
                node = node.right
        return result

