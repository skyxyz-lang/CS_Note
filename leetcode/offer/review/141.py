#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 141.py
@time: 2021/1/23 16:22
@source: https://leetcode-cn.com/problems/linked-list-cycle/
@desc: 141. 环形链表
"""
# 思路，环形链表一般使用快慢指针，快指针每次走两步，慢指针每次走一步，如果快指针能追上慢指针则有环，否则无环


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        slow = head
        fast = head.next
        while fast and fast.next:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next
        return False
