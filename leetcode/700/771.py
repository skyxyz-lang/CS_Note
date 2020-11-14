#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 771.py
@time: 2020/10/10 15:19
@desc:
"""


class Solution(object):

    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        ans = 0
        dic = {}
        for a in J:
            dic[a] = 1
        for b in S:
            if b in dic:
                ans += 1
        return ans
