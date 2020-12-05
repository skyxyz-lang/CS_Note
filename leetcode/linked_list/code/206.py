#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 206.py
@time: 2020/12/5 21:02
@source: https://leetcode-cn.com/problems/reverse-linked-list/
@desc: 206. 反转链表
"""
from list_node import ListNode


class Solution(object):
    """

    """
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 递归法
        if not head or not head.next:
            return head
        next_node = head.next
        cur = self.reverseList(head.next)
        next_node.next = head
        head.next = None
        return cur

    def reverseList2(self, head):
        """
        原地反转法
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        # 加上防止循环
        pre.next = None
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseList3(self, head):
        """

        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        cur = head
        pre = None
        while cur:
            ne_next = cur.next
            cur.next = pre
            pre = cur
            cur = ne_next
        return pre
