#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 13.py
@time: 2021/1/17 11:55
@source: https://leetcode-cn.com/problems/ji-qi-ren-de-yun-dong-fan-wei-lcof/
@desc: 剑指 Offer 13. 机器人的运动范围
"""
# 思路，可以看成二叉树的层序遍历，一层一层获取结果，注意需要记录访问结果


class Solution(object):
    def movingCount(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 1
        queue = []
        visited = [[False for i in range(n)] for j in range(m)]
        step_x = [1, -1, 0, 0]
        step_y = [0, 0, 1, -1]
        # 初始化
        result_num = 0
        queue.append((0, 0))
        while len(queue) > 0:
            x, y = queue.pop(0)
            visited[x][y] = True
            result_num += 1
            for i in range(4):
                pos_x = x + step_x[i]
                pos_y = y + step_y[i]
                if 0 <= pos_x < m and 0 <= pos_y < n and self.is_validate_k(pos_x, pos_y, k) and not \
                        visited[pos_x][pos_y]:
                    visited[pos_x][pos_y] = True
                    queue.append((pos_x, pos_y))
        return result_num

    def is_validate_k(self, m, n, k):
        """

        :param m:
        :param n:
        :param k:
        :return:
        """
        s = str(m) + str(n)
        sum_all = 0
        for i in s:
            sum_all += int(i)
            if sum_all > k:
                return False
        return True


if __name__ == '__main__':
    obj = Solution()
    print obj.movingCount(2, 3, 17)