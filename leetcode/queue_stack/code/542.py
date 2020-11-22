#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 542.py
@time: 2020/11/22 21:56
@source:https://leetcode-cn.com/problems/01-matrix/
@desc:542. 01 矩阵
"""
import collections


class Solution(object):
    """

    """
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        rows = len(matrix)
        cols = len(matrix[0])
        result = [[0 for i in range(cols)] for j in range(rows)]
        step_x = [0, 0, 1, -1]
        step_y = [1, -1, 0, 0]
        st = collections.deque()
        for i in range(rows):
            for j in range(cols):
                st.append((i, j, 0))
                while len(st) > 0:
                    cur_x, cur_y, depth = st.popleft()
                    if matrix[cur_x][cur_y] == 0:
                        result[i][j] = depth
                        st = collections.deque()
                        break
                    for k in range(4):
                        x = cur_x + step_x[k]
                        y = cur_y + step_y[k]
                        if 0 <= x < rows and 0 <= y < cols:
                            st.append((x, y, depth + 1))
        return result


if __name__ == '__main__':
    obj = Solution()
    print obj.updateMatrix([[0,0,0],[0,1,0],[1,1,1]])