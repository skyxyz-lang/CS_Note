#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 1022.py
@time: 2020/11/21 17:40
@source:https://leetcode-cn.com/problems/sum-of-root-to-leaf-binary-numbers/
@desc: 从根到叶的二进制数之和
"""
from tree_node import TreeNode
import math


class Solution(object):
    """

    """
    def __init__(self):
        self.path_lst = []

    def sumRootToLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.trvael(root, "")
        sum_val = 0
        for i in self.path_lst:
            sum_val += self.convert_num(i)
        return sum_val

    def trvael(self, root, path):
        """

        :param root:
        :param path:
        :return:
        """
        if not root:
            return
        if not root.left and not root.right:
            self.path_lst.append(path + str(root.val))
            return
        path = path + str(root.val)
        self.trvael(root.left, path)
        self.trvael(root.right, path)

    def convert_num(self, num_str):
        """

        :param num_str:
        :return:
        """
        num = 0

        for i in range(len(num_str)):
            index = len(num_str) - i - 1
            num += int(num_str[index]) * 2**i
        return num


if __name__ == '__main__':
    obj = Solution()
    print obj.convert_num("100")