#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: ab_sq.py
@time: 2020/11/18 22:45
@desc:
https://leetcode-cn.com/leetbook/read/queue-stack/kfgtt/
"""
import collections


class Solution(object):
    """

    """

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        k = n
        used = {}
        queue = collections.deque([(n, 0)])
        used[n] = 1
        while len(queue) > 0:
            print queue
            (n, depth) = queue.popleft()
            if n == 0:
                return depth
            for i in range(1, (k+1)/2 + 1):
                sq = i * i
                re = n - sq
                if re > 0 and re not in used:
                    used[re] = 1
                    queue.append((n-sq, depth + 1))
                elif re == 0:
                    return depth + 1
        return -1


if __name__ == '__main__':
    obj = Solution()
    print obj.numSquares(13)




