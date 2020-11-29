#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: merge.py
@time: 2020/11/29 10:03
@source: 归并排序 空间O(N) 时间 O(log2n)
@desc:
"""


def merge_sort(arr):
    """
    归并排序, 思路主要是先拆后和
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    mid = len(arr) / 2
    left = arr[0:mid]
    right = arr[mid:]
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    """
    left和right都是有序的
    :param left:
    :param right:
    :return:
    """
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] < right[0]:
            res.append(left[0])
            left.pop(0)
        else:
            res.append(right[0])
            right.pop(0)
    while len(left) > 0:
        res.append(left[0])
        left.pop(0)
    while len(right) > 0:
        res.append(right[0])
        right.pop(0)
    return res


print merge_sort([4, 3, 6, 8, 2, 3, 1, 7, 10, 19, -10])
