#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: quick.py
@time: 2020/11/29 10:24
@source:  快速排序，分治法
@desc: 空间复杂度O(1),时间复杂度O(log2n) 不稳定
"""


def quick_sort(arr, left, right):
    """

    :param arr:
    :param left:
    :param right:
    :return:
    """
    l = left
    r = right
    if left > right:
        return
    point = arr[left]
    while left < right:
        while left < right and arr[right] >= point:
            right -= 1
        if left < right:
            arr[left] = arr[right]
            left += 1
        while left < right and arr[left] < point:
            left += 1
        if left < right:
            arr[right] = arr[left]
            right -= 1
    arr[left] = point
    # 递归调用，由于第一次确定了锚点，所以锚点的顺序已定，不需要额外的排序，对于锚点左右进行排序即可
    quick_sort(arr, l, left - 1)
    quick_sort(arr, left + 1, r)
    return arr


lst = [4, 3, 6, 8, 2, 3, 1, 7, 10, 19, -10]
print quick_sort(lst, 0, len(lst) - 1)


