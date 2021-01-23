#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 12.py
@time: 2021/1/16 22:24
@source: https://leetcode-cn.com/problems/ju-zhen-zhong-de-lu-jing-lcof/
@desc: 剑指 Offer 12. 矩阵中的路径
"""
# 思路 遍历整个board，以每个board为起点，搜索word，搜索到返回true，否则返回false
# 以每个board为起点的搜索，需要记录搜索过得路径，使用一个visited数组


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        m = len(board)
        n = len(board[0])
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if self.dfs_search(visited, board, i, j, 0, word):
                    return True
        return False

    def dfs_search(self, visited, board, cur_x, cur_y, index, word):
        """

        :param visited:
        :param board:
        :param cur_x:
        :param cur_y:
        :param index:
        :param word:
        :return:
        """
        m = len(board)
        n = len(board[0])
        dp_x = [-1, 1, 0, 0]
        dp_y = [0, 0, 1, -1]
        if index == len(word) - 1:
            return board[cur_x][cur_y] == word[index]
        if board[cur_x][cur_y] == word[index]:
            visited[cur_x][cur_y] = True
            for i in range(4):
                x = cur_x + dp_x[i]
                y = cur_y + dp_y[i]
                if 0 <= x < m and 0 <= y < n and not visited[x][y] and self.dfs_search(visited, board, x, y, index+1, word):
                    return True
            visited[cur_x][cur_y] = False
        return False








