#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: choose.py
@time: 2020/11/25 23:11
@source: 空间O(1) 时间O(n*n)
@desc: 选择排序
"""


def choose_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(i, length):
            current_min = i
            if arr[current_min] > arr[j]:
                current_min = j
            tmp = arr[i]
            arr[i] = arr[current_min]
            arr[current_min] = tmp
    return arr


print choose_sort([4, 3, 6, 8, 2, 3, 1])
