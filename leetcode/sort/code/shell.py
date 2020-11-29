#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: shell.py
@time: 2020/11/25 23:46
@source: 希尔排序，带有gap的插入排序  不稳定 时间O(n1.3) 空间O(1)
@desc:
"""


def shell_sort(arr):
    """

    :param arr:
    :return:
    """
    length = len(arr)
    for gap in reversed(range(1, 9, 2)):
        for i in range(gap, length, gap):
            pre_index = i - gap
            current = arr[i]
            while pre_index >= 0 and arr[pre_index] > current:
                arr[pre_index + gap] = arr[pre_index]
                pre_index -= gap
            arr[pre_index + gap] = current
    return arr


print shell_sort([4, 3, 6, 8, 2, 3, 1, 7, 10, 19, -10])