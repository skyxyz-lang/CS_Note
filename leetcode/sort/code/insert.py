#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: insert.py
@time: 2020/11/25 23:16
@source: 空间O(1) 时间O(n*n) 不稳定
@desc: 插入排序
"""


def insert_sort(arr):
    length = len(arr)
    for i in range(1, length):
        pre_index = i - 1
        current = arr[i]
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr


print insert_sort([4, 3, 6, 8, 2, 3, 1, 7, 10, 19, -10])
