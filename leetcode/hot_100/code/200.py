#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 200.py
@time: 2020/12/13 10:15
@source: https://leetcode-cn.com/problems/number-of-islands/
@desc: 200. 岛屿数量
"""
# 每个岛屿被水包围，求出岛屿的数量其实就是求出不临接的1的数量
# 可以采用DFS方案以及BFS方案进行遍历，下面分别分析两种方案
# BFS 采用队列 ，DFS采用栈或者递归都行
# 1、采用队列保存遍历过程中的相邻可达节点首先把当前有效节点放入队列中
# 2、判断队列是否为空，出队进行访问，并且寻找相邻的4个有效节点，放入队列中。
# 3、当前的队列为空则代表一个岛屿已经找到，继续寻找下一个目标目标节点


class Solution(object):
    """

    """
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        m = len(grid)
        n = len(grid[0])
        step_x = [1, -1, 0, 0]
        step_y = [0, 0, 1, -1]
        queue = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    count += 1
                    queue.append((i, j))
                while len(queue) > 0:
                    cur_x, cur_y = queue.pop(0)
                    grid[cur_x][cur_y] = "0"
                    for k in range(4):
                        x = cur_x + step_x[k]
                        y = cur_y + step_y[k]
                        if m > x >= 0 and n > y >= 0 and grid[x][y] == "1":
                            queue.append((x, y))
        return count
