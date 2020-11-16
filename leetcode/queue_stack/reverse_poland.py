#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: reverse_poland.py
@time: 2020/11/17 23:46
@desc: 逆波兰表达式
https://leetcode-cn.com/leetbook/read/queue-stack/gomvm/
"""


class Solution(object):
    """

    """
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        st_value = []
        for v in tokens:
            if v in ["+", "-", "*", "/"]:
                value2 = int(st_value.pop())
                value1 = int(st_value.pop())
                symbol = v
                if symbol == '*':
                    value = value1 * value2
                elif symbol == '-':
                    value = value1 - value2
                elif symbol == '+':
                    value = value1 + value2
                elif symbol == "/":
                    if value1 * value2 > 0:
                        value = value1 // value2
                    else:
                        value = -(-value1 / value2)
                st_value.append(value)
            else:
                st_value.append(v)
        return int(st_value.pop())


if __name__ == '__main__':
    obj = Solution()
    print obj.evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])