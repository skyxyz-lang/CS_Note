#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: findk.py
@time: 2020/12/8 16:31
@source:https://www.jianshu.com/p/33ee33ce8699
@desc: 第k大数
"""


def find_k(array, k, left, right):
    """
    寻找第k大数
    :param array:
    :param k:
    :param left:
    :param right:
    :return:
    """
    index = partition(array, left, right)
    if index == k-1:
        return array[k-1]
    elif index > k-1:
        return find_k(array, k, left, index-1)
    elif index < k-1:
        return find_k(array, k, index+1, right)
    return 0

def partition(arr, left, right):
    """
    分治
    :param arr:
    :param left:
    :param right:
    :return:
    """
    if left > right:
        return
    point = arr[left]
    while left < right:
        while left < right and point >= arr[right]:
            right -= 1
        if left < right:
            arr[left] = arr[right]
            left += 1
        while left < right and point < arr[left]:
            left += 1
        if left < right:
            arr[right] = arr[left]
            right -= 1
    arr[left] = point
    return left


a = [4, 3, 2, 1, 5, 6, 7, 8]
print find_k(a, 5, 0, len(a)-1)


