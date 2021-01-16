#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 4.py
@time: 2021/1/16 17:14
@source: https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/
@desc: 剑指 Offer 04. 二维数组中的查找
"""
# 思路：该matrix站在右上角来看是个二叉搜索树，使用递归即可找到结果


class Solution(object):
    def findNumberIn2DArray(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return True
        n = len(matrix[0])
        return self.binary_tree_search(matrix, 0, n-1, target)

    def binary_tree_search(self, matrix, top, right, target):
        """

        :param matrix:
        :param top:
        :param right:
        :param target:
        :return:
        """
        m = len(matrix)
        n = len(matrix[0])
        if 0 <= top < m and 0 <= right < n:
            if matrix[top][right] == target:
                return True
            elif matrix[top][right] > target:
                return self.binary_tree_search(matrix, top, right-1, target)
            else:
                return self.binary_tree_search(matrix, top+1, right, target)
        else:
            return False
