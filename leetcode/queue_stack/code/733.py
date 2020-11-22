#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 733.py
@time: 2020/11/22 21:36
@source: https://leetcode-cn.com/problems/flood-fill/
@desc:733. 图像渲染
"""
import collections


class Solution(object):
    """

    """
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        queue = collections.deque([(sr, sc)])
        old_color = image[sr][sc]
        if old_color == newColor:
            return image
        step_x = [0, 0, 1, -1]
        step_y = [1, -1, 0, 0]
        rows = len(image)
        cols = len(image[0])
        while len(queue) > 0:
            cur_x, cur_y = queue.popleft()
            image[cur_x][cur_y] = newColor
            for i in range(4):
                x = cur_x + step_x[i]
                y = cur_y + step_y[i]
                if 0 <= x < rows and 0 <= y < cols and image[x][y] == old_color:
                    queue.append((x, y))
        return image


if __name__ == '__main__':
    obj = Solution()
    print obj.floodFill([[0,0,0],[0,1,1]] , 1, 1, 1)
