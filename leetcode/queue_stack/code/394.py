#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 394.py
@time: 2020/11/22 21:07
@source: https://leetcode-cn.com/problems/decode-string/
@desc: 394. 字符串解码
"""


class Solution(object):
    """

    """
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num_set = {'1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}
        st = []
        for i in s:
            if i in num_set:
                st.append(i)
            elif i == '[':
                st.append(i)
            elif i == ']':
                tmp_str = ''
                while st[-1] != '[':
                    tmp_str = st.pop() + tmp_str
                st.pop()
                num_str = ""
                while len(st) > 0 and st[-1] in num_set:
                    num_str = st.pop() + num_str
                times = int(num_str)
                tmp_str = tmp_str * times
                st.append(tmp_str)
            else:
                st.append(i)
        res = ""
        while len(st) > 0:
            res = st.pop() + res
        return res


if __name__ == '__main__':
    obj = Solution()
    print obj.decodeString("100[leetcode]")