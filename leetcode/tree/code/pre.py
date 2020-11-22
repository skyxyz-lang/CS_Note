#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: pre.py
@time: 2020/11/14 09:47
@desc:
"""


class TreeNode(object):
    """
    二叉树的节点定义以及前序遍历
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):

    def preorderTraversal(self, root):
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
        lst.append(root.val)
        self.travel(root.left, lst)
        self.travel(root.right, lst)

    def pre_order_no_dfs(self, root):
        """
        非递归前序遍历
        :param root:
        :return:
        """
        if not root:
            return []
        result = []
        st = [root]
        while len(st) > 0:
            node = st.pop()
            result.append(node.val)
            if node.right:
                st.append(node.right)
            if node.left:
                st.append(node.left)
        return result
