#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: islands_count.py
@time: 2020/11/15 19:36
@desc:
https://leetcode-cn.com/leetbook/read/queue-stack/gpfm5/
"""
from Queue import Queue


class Solution(object):
    """
    孤岛问题
    """
    def numIslands(self, grid):
        """
        bfs
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        if len(grid) < 1:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        step_x = [0, 0, 1, -1]
        step_y = [1, -1, 0, 0]
        queues = Queue()
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    queues.put((i, j))
                    grid[i][j] = 0
                    while queues.qsize() > 0:
                        (index_x, index_y) = queues.get(0)
                        for k in range(4):
                            x = index_x + step_x[k]
                            y = index_y + step_y[k]
                            if 0 <= x < rows and 0 <= y < cols and grid[x][y] == "1":
                                queues.put((x, y))
                                grid[x][y] = 0
        return count

    def numIslands_dfs(self, grid):
        """

        :param grid:
        :return:
        """
        count = 0
        if len(grid) < 1:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1":
                    count += 1
                    self.dfs(grid, i, j, rows, cols)
        return count

    def dfs(self, grid, x, y, rows, cols):
        """

        :param grid:
        :param x:
        :param y:
        :param rows:
        :param cols:
        :return:
        """
        grid[x][y] = 0
        step_x = [0, 0, 1, -1]
        step_y = [1, -1, 0, 0]
        for i in range(4):
            k1 = x + step_x[i]
            k2 = y + step_y[i]
            if 0 <= k1 < rows and 0 <= k2 < cols and grid[k1][k2] == "1":
                self.dfs(grid, k1, k2, rows, cols)


if __name__ == '__main__':
    obj = Solution()
    print obj.numIslands([["1","1","1","1","1","1","1"]])