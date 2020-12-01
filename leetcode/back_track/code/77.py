#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 77.py
@time: 2020/12/1 23:03
@source:  https://leetcode-cn.com/problems/combinations/
@desc: 77. 组合
"""
from copy import deepcopy


class Solution(object):
    """

    """
    def __init__(self):
        self.final_result = []

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        self.back_track(n, k, 1, [])
        return self.final_result

    def back_track(self, n, k, start, cur_path):
        if len(cur_path) == k:
            self.final_result.append(deepcopy(cur_path))
            return
        for i in range(start, n+1):
            # 每个数只能使用一次
            cur_path.append(i)
            self.back_track(n, k, i + 1, cur_path)
            cur_path.pop()


if __name__ == '__main__':
    obj = Solution()
    print obj.combine(4, 2)