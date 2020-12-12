#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: test.py
@time: 2020/12/8 20:19
@source:
@desc:
"""


def run(nums):
    index = len(nums) - 1
    while index > 0 and nums[index] <= nums[index-1]:
        index -= 1
    if index == 0:
        return reversed(nums)
    else:
        i = len(nums) - 1
        while i > 0 and nums[i] <= nums[index -1]:
            i += 1
        tmp = nums[i]
        nums[i] = nums[index-1]
        nums[index-1] = tmp
        print nums
        res = nums[0:index] + list(reversed(nums[index: -1]))
        return res


print run([8, 7, 6, 3, 6, 5])