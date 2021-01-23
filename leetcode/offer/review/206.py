#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 206.py
@time: 2021/1/23 16:01
@source: https://leetcode-cn.com/problems/reverse-linked-list/
@desc: 206. 反转链表
"""
# 原地反转两种方式，一种是递归法，一种是迭代法
from list_node import ListNode


class Solution(object):
    def reverseList(self, head):
        """
        迭代法，原地反转
        :type head: ListNode
        :rtype: ListNode
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

    def reverseList2(self, head):
        """
        递归法
        :param head:
        :return:
        """
        if not head or not head.next:
            return head
        nxt = head.next
        reverse = self.reverseList2(head.next)
        head.next = None
        nxt.next = head
        return reverse


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    a.next = b
    b.next = c
    c.next = d
    obj = Solution()
    e = obj.reverseList2(a)
    while e:
        print e.val
        e = e.next
