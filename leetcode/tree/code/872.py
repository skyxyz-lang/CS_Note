#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 872.py
@time: 2020/11/21 18:29
@source: https://leetcode-cn.com/problems/leaf-similar-trees/
@desc: 叶子相似的树
"""
from tree_node import TreeNode


class Solution(object):
    """

    """

    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        lst1 = self.travel(root1, [])
        lst2 = self.travel(root2, [])
        if len(lst1) != len(lst2):
            return False
        for i in range(len(lst1)):
            if lst1[i] != lst2[i]:
                return False
        return True

    def travel(self, root, store_lst):
        """

        :param root:
        :param store_lst:
        :return:
        """
        if not root:
            return
        if not root.left and not root.right:
            store_lst.append(root.val)
        self.travel(root.left, store_lst)
        self.travel(root.right, store_lst)
        return store_lst
