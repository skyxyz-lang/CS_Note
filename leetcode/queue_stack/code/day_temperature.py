#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: day_temperature.py
@time: 2020/11/17 23:27
@desc: 每日温度
https://leetcode-cn.com/leetbook/read/queue-stack/genw3/
"""


class Solution(object):
    """

    """
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        result = [0] * len(T)
        st = []
        for i in range(len(T)):
            cur_val = T[i]
            while len(st) > 0 and T[st[-1]] < cur_val:
                index = st.pop()
                result[index] = i - index
            st.append(i)
        return result


if __name__ == '__main__':
    obj = Solution()
    print obj.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73])