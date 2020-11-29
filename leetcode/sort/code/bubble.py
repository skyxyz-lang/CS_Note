#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: bubble.py
@time: 2020/11/25 23:03
@source: 空间 O(1)  时间O(n*n)
@desc: 冒泡排序
"""


def bubble_sort(arr):
    length = len(arr)
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] > arr[j+1]:
                tmp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = tmp
    return arr


print bubble_sort([4, 3, 6, 8, 2, 3, 1])
