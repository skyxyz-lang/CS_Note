#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: sort.py
@time: 2021/1/23 20:11
@source:
@desc: 排序算法
"""
import sys


class Solution(object):

    def __init__(self):
        pass

    def quick_sort(self, lst, left, right):
        """
        快速排序
        思路：挖坑法
        1、整体思路是选择一个锚点，把比锚点大的数据放到右边，比锚点小的数据放到左边
        2、从右边开始，找到第一个比锚点小的数，然后放到左边的坑，这样右边多了一个坑
        3、在从左边开始，找到第一个比锚点大的数，放大右边的坑，这样左边多了一个坑
        4、重复 2-3，直到 列表达到1所描述的状态，然后递归求解。
        时间复杂度，平均n(logn),空间复杂度O(1)，不稳定
        :param lst:
        :param left:
        :param right:
        :return:
        """
        l = left
        r = right
        if left > right:
            return
        pov = lst[left]
        while left < right:
            while left < right and lst[right] >= pov:
                right -= 2
            if left < right:
                lst[left] = lst[right]
                left += 1
            while left < right and lst[left] < pov:
                left += 1
            if left < right:
                lst[right] = lst[left]
                right -= 1
        lst[left] = pov
        self.quick_sort(lst, l, left-1)
        self.quick_sort(lst, left+1, r)
        return lst

    def bubble_sort(self, lst):
        """
        冒泡排序
        1、冒泡排序主要是比较元素，每次从头开始，拿当前元素与后一个元素比较，交换，把最大的放到最后，每次确定一个最大元素的位置，直到遍历n
        次，确定n个元素的位置为止
        时间复杂度 O(n*n),空间复杂度O(1)
        :param lst:
        :return:
        """
        for i in range(len(lst)):
            for j in range(len(lst) - i - 1):
                if lst[j] > lst[j+1]:
                    tmp = lst[j]
                    lst[j] = lst[j+1]
                    lst[j+1] = tmp
        return lst

    def choose_sort(self, lst):
        """
        选择排序
        选择排序是 把当前序列看成两个部分，分别为排序好的部分和未排序的部分
        每次从未排序的部分选择当前最小的插入已排序部分的后面，以实现选择排序
        :param lst:
        :return:
        """
        for i in range(len(lst)):
            current_min = i
            for j in range(i, len(lst)):
                if lst[current_min] > lst[j]:
                    current_min = j
                    tmp = lst[i]
                    lst[i] = lst[j]
                    lst[current_min] = tmp
        return lst

    def merge_sort(self, lst):
        """
        归并排序
        :param lst:
        :return:
        """
        if len(lst) < 2:
            return lst
        mid = len(lst)/2
        left = lst[0:mid]
        right = lst[mid:]
        return self.merge_sort_help(self.merge_sort(left), self.merge_sort(right))

    def merge_sort_help(self, left, right):
        """

        :param left:
        :param right:
        :return:
        """
        lst = []
        l = 0
        r = 0
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                lst.append(left[l])
                l += 1
            else:
                lst.append(right[r])
                r += 1
        while l < len(left):
            lst.append(left[l])
            l += 1
        while r < len(right):
            lst.append(right[r])
            r += 1
        return lst

    def heap_sort(self, lst):
        """
        堆排序
        1、堆排序利用堆的性质，先进性建堆，大顶堆，然后交换堆顶和末尾的元素，在进行堆的调整，堆可以看成一颗二叉树，对于数组，该二叉树有如下性质
        2、节点j的左右孩子节点分别为 2j 和 2j+1
        3、数组的第一个非叶子节点为 length / 2  -1
        4、堆排序最重要的是堆调整的过程，并且堆调整是一个递归的过程
        :param lst:
        :return:
        """
        arr = self.build_heap(lst)
        length = len(arr)
        while length > 0:
            tmp = arr[length - 1]
            arr[length - 1] = arr[0]
            arr[0] = tmp
            length -= 1
            self.adjust_heap(arr, 0, length)
        return arr

    def adjust_heap(self, arr, target, length):
        """
        调整第i个元素
        :param arr:
        :param i:
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
            self.adjust_heap(arr, max_index, length)

    def build_heap(self, arr):
        """
        建堆的过程是从第一个非叶子节点开始调整堆
        :param arr:
        :return:
        """
        index = len(arr)/2-1
        while index >= 0:
            self.adjust_heap(arr, index, len(arr))
            index -= 1
        return arr

    def insert_sort(self, lst):
        """
        插入排序
        1、把待排序的数组看成两部分，左边是已排序，右边是未排序，每次从未排序的里面选择一个数，插入到已排序的序列的合适的位置
        :param lst:
        :return:
        """
        for i in range(1, len(lst)):
            v = lst[i]
            pre_index = i-1
            while pre_index >= 0 and lst[pre_index] > v:
                lst[pre_index+1] = lst[pre_index]
                pre_index -= 1
            lst[pre_index + 1] = v
        return lst


if __name__ == '__main__':
    to_be_sort = [1, 2, 7, 3, 9, 10, 31, 0, -1]
    obj = Solution()
    #print obj.quick_sort(to_be_sort, 0, len(to_be_sort)-1)
    #print obj.bubble_sort(to_be_sort)
    #print obj.choose_sort(to_be_sort)
    #print obj.merge_sort(to_be_sort)
    #print obj.merge_sort_help([1, 4], [-1, 2])
    print obj.heap_sort(to_be_sort)
