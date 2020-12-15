#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 143.py
@time: 2020/12/12 22:14
@source: https://leetcode-cn.com/problems/reorder-list/
@desc: 143. 重排链表
"""
from list_node import ListNode


class Solution(object):
    """

    """
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return head
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        move = length / 2
        cur = head
        pre = head
        while move > 0:
            pre = cur
            cur = cur.next
            move -= 1
        pre.next = None
        head2 = self.reverse(cur)
        cur = head
        while cur and head2:
            tmp1 = cur.next
            tmp2 = head2.next
            cur.next = head2
            if tmp1:
                head2.next = tmp1
            cur = tmp1
            head2 = tmp2
        return head

    def reverse(self, head):
        """
        翻转链表
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        head_next = head.next
        nt = self.reverse(head.next)
        head_next.next = head
        head.next = None
        return nt
