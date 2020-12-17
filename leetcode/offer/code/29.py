#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 29.py
@time: 2020/12/16 23:18
@source: https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/
@desc: 剑指 Offer 29. 顺时针打印矩阵
"""
# 思路
# 按照一圈一圈的思路打印，选定上下左右四个点
# 沿着top从左到右，  top++
# 沿着right，从上到下，right--
# 沿着bottom，从右到左 button++
# 沿着left， 从下到上，left ++

# 遍历过程满足 left <=right  top <= bottom


class Solution(object):

    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        top = 0
        left = 0
        right = len(matrix[0])
        bottom = len(matrix)
        res = [0] * (right * bottom)
        index = 0
        right = right - 1
        bottom = bottom - 1
        while left <= right and top <= bottom:
            i = left
            while i <= right:
                res[index] = matrix[top][i]
                index += 1
                i += 1
            top += 1
            i = top
            while i <= bottom:
                res[index] = matrix[i][right]
                index += 1
                i += 1
            right -= 1
            i = right
            while i >= left and top <= bottom:
                res[index] = matrix[bottom][i]
                index += 1
                i -= 1
            bottom -= 1
            i = bottom
            while i >= top and left <= right:
                res[index] = matrix[i][left]
                index += 1
                i -= 1
            left += 1
        return res


if __name__ == '__main__':
    obj = Solution()
    print obj.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
