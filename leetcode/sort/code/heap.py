#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: heap.py
@time: 2020/11/29 10:46
@source: 堆排序,堆排序主要分如下几步，1、建堆 2、交换 3、调整 其中核心功能是调整堆
@desc: 时间(log2n) 空间O(1)
"""
import sys
# 堆可以看成一颗完全二叉树，在数组中有如下的性质
# 堆的第一个非叶子节点为 floor(len(arr)/2) - 1  floor 为向下取整的函数
# 对于非叶子节点i，其左右的叶子节点分别如下(如果存在的话): left=2*i+1 right = 2*i+2
# 排序使用的是大顶堆，其满足一个二叉树的左右孩子都比根节点小
# 建堆的过程是从第一个非叶子节点进行调整的


def adjust_heap(arr, target, length):
    """
    调整堆
    :param arr:
    :param target:
    :param length:
    :return:
    """
    left = 2 * target + 1
    right = 2 * target + 2
    max_index = target
    max_value = arr[target]
    if left < length and arr[left] > max_value:
        max_index = left
        max_value = arr[left]
    if right < length and arr[right] > max_value:
        max_index = right
        max_value = arr[right]
    if max_index != target:
        arr[max_index] = arr[target]
        arr[target] = max_value
        # 如果有交互，则需要递归调整
        adjust_heap(arr, max_index, length)
    return arr


def heap_sort(arr):
    """
    堆排序
    :param arr:
    :return:
    """
    length = len(arr)
    index = length / 2 - 1
    while index >= 0:
        adjust_heap(arr, index, length)
        index -= 1
    while length > 0:
        tmp = arr[length - 1]
        arr[length - 1] = arr[0]
        arr[0] = tmp
        length -= 1
        adjust_heap(arr, 0, length)
    return arr


print heap_sort([4, 3, 6, 8, 2, 3, 1, 7, 10, 19, -10])





