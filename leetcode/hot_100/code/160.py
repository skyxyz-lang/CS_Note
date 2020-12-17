#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 160.py
@time: 2020/12/17 22:21
@source: https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
@desc: 160. 相交链表
"""
# A B同时往前走，到达结尾的时候A、B交换，如果有交点那么A、B最终相遇，如果无交点，不会碰到
from list_node import ListNode


class Solution(object):
    """

    """
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        head_a = headA
        head_b = headB
        while head_a != head_b:
            if not head_a:
                head_a = headB
            else:
                head_a = head_a.next
            if not head_b:
                head_b = headA
            else:
                head_b = head_b.next
        return head_a
