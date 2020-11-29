#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: decorator.py
@time: 2020/11/29 12:01
@source:
@desc:
"""
import time
import sys

def use_logging(func):
    """
    :param func:
    :return:
    """
    def wap(*args, **kwargs):
        st_time = time.time()
        res = func(*args, **kwargs)
        ed_time = time.time()
        print func.__name__ + 'is execute %ss' % str(ed_time - st_time)
        return res
    return wap


@use_logging
def add(a, b):
    print a + b
    return a + b


class A(object):

    def __init__(self, a):
        self.a = a


objA = A(1)
print sys.getrefcount(objA)
a = [objA]
print sys.getrefcount(objA)
