#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: n_tree_node.py
@time: 2020/11/21 10:15
@desc: N叉树节点定义
@source:
"""


class Node(object):

    def __init__(self, val=None, children=None):
        """

        :param val:
        :param children:
        """
        self.val = val
        self.children = children
