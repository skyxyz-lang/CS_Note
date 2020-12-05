#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 141.py
@time: 2020/12/5 21:27
@source: https://leetcode-cn.com/problems/linked-list-cycle/
@desc: 141. 环形链表
"""
from list_node import ListNode


class Solution(object):
    """

    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next or not head.next.next:
            return False
        slow = head
        fast = head
        while slow and fast:
            slow = slow.next
            if not fast.next:
                return False
            fast = fast.next.next
            if slow == fast:
                return True
        return False



