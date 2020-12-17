#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 142.py
@time: 2020/12/17 22:46
@source: https://leetcode-cn.com/problems/linked-list-cycle-ii/
@desc: 142. 环形链表 II
"""
# 快慢指针找到环形相交节点之后，slow节点到交点的距离等于头节点到交点的距离

from list_node import ListNode


class Solution(object):
    """

    """
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return None
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        if fast:
            fast = head
            while slow and fast:
                if slow == fast:
                    return slow
                slow = slow.next
                fast = fast.next
        return None
