#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 6.py
@time: 2021/1/16 19:33
@source: https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof/
@desc: 剑指 Offer 06. 从尾到头打印链表
"""
# 先反转，再输出，时间复杂度o(n)，空间复杂度 O(1)
from list_node import ListNode


class Solution(object):
    """

    """
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if not head:
            return []
        head = self.reverseLinkedList(head)
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
        return lst

    def reverseLinkedList(self, head):
        """

        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        pre = None
        while head:
            current = head
            head = head.next
            current.next = pre
            pre = current
        return pre




