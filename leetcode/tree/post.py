#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: post.py
@time: 2020/11/14 10:44
@desc:
"""


class TreeNode(object):
    """
    二叉树的节点定义以及后续遍历
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    """

    """

    def postorderTraversal(self, root):
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
            return []
        self.travel(root.left, lst)
        self.travel(root.right, lst)
        lst.append(root.val)

    def post_oder_no_dfs(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return []
        st = [root]
        result = []
        while len(st) > 0:
            node = st.pop()
            result.append(node.val)
            if node.left:
                st.append(node.left)
            if node.right:
                st.append(node.right)
        result.reverse()
        return result
