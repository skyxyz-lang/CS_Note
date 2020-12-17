#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 21.py
@time: 2020/12/17 23:16
@source: https://leetcode-cn.com/problems/merge-two-sorted-lists/
@desc: 21. 合并两个有序链表
"""
from list_node import ListNode


class Solution(object):
    """

    """
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        cur = dummy
        while l1 and l2:
            if l1.val > l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        while l1:
            cur.next = l1
            l1 = l1.next
            cur = cur.next
        while l2:
            cur.next = l2
            l2 = l2.next
            cur = cur.next
        return dummy.next
