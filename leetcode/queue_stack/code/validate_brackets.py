#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: validate_brackets.py
@time: 2020/11/16 23:53
@desc:有效的括号
https://leetcode-cn.com/leetbook/read/queue-stack/g9d0h/
"""


class Solution(object):
    """

    """
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        mp = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        st = []
        flag = True
        for c in s:
            if c == '(' or c == '[' or c == '{':
                st.append(c)
            elif c == ')' or c == ']' or c == '}':
                if len(st) <= 0:
                    flag = False
                    break
                e = st.pop()
                if mp.get(e) != c:
                    flag = False
                    break
        if len(st) > 0:
            flag = False
        return flag
