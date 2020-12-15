#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 79.py
@time: 2020/12/12 22:51
@source: https://leetcode-cn.com/problems/word-search/
@desc: 79. 单词搜索
"""
# 1、矩阵中搜索单词，主要是通过dfs进行搜索
# 2、需要对于矩阵每个位置为开头的地方进行搜索
# 3、搜索函数需要记录当前搜索的状态以及进行回溯


class Solution(object):
    """

    """

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m = len(board)
        n = len(board[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if self.back_track(visited, board, i, j, 0, word):
                    return True
        return False

    def back_track(self, visited, board, curx, cury, index, word):
        m = len(board)
        n = len(board[0])
        step_x = [1, -1, 0, 0]
        step_y = [0, 0, 1, -1]
        if index == len(word) - 1:
            return board[curx][cury] == word[index]
        if board[curx][cury] == word[index]:
            visited[curx][cury] = 1
            for i in range(4):
                x = curx + step_x[i]
                y = cury + step_y[i]
                if 0 <= x < m and 0 <= y < n and visited[x][y] == 0 and self.back_track(visited, board, x, y, index+1, word):
                    return True
            visited[curx][cury] = 0
        return False






