#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 563.py
@time: 2020/11/21 22:12
@source:https://leetcode-cn.com/problems/binary-tree-tilt/
@desc:二叉树的坡度
"""
from tree_node import TreeNode


class Solution(object):
    """

    """
    def __init__(self):
        self.tile_lst = []
        self.tile_dic = {}

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.travel_tilt(root)
        print self.tile_dic
        return sum(self.tile_lst)

    def travel_tilt(self, root):
        """

        :param root:
        :return:
        """
        if not root:
            return 0
        # 分别计算左右节点之和
        left = self.travel_tilt(root.left)
        right = self.travel_tilt(root.right)
        tilt = abs(left - right)
        self.tile_lst.append(tilt)
        self.tile_dic[root.val] = tilt
        return left + right + root.val
