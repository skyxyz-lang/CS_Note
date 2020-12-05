#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: offer-52.py
@time: 2020/12/5 21:35
@source: https://leetcode-cn.com/problems/liang-ge-lian-biao-de-di-yi-ge-gong-gong-jie-dian-lcof/
@desc: 剑指 Offer 52. 两个链表的第一个公共节点
"""
from list_node import ListNode


class Solution(object):
    """

    """
    def getIntersectionNode(self, headA, headB):
        """
        :type headA, headB: ListNode
        :rtype: ListNode
        """
        len_a = self.len_list(headA)
        len_b = self.len_list(headB)
        if len_a > len_b:
            gap = len_a - len_b
            while gap > 0:
                headA = headA.next
                gap -= 1
        else:
            gap = len_b - len_a
            while gap > 0:
                headB = headB.next
                gap -= 1
        while headA and headB:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

    def len_list(self, head):
        """

        :param head: ListNode
        :return:
        """
        cur = 0
        while head:
            cur += 1
            head = head.next
        return cur
