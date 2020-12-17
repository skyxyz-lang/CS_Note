#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 234.py
@time: 2020/12/15 23:06
@source: https://leetcode-cn.com/problems/palindrome-linked-list/
@desc: 234. 回文链表
"""
# 遍历到中点，然后反转链表进行比较
# 找到链表中点使用快慢指针法
# 反转链表采用原地反转法
from list_node import ListNode


class Solution(object):
    """

    """
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return True
        if not head.next:
            return True
        slow = head
        fast = head
        # 1、奇数个节点则寻找到中点，偶数个节点则寻找到n/2
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        head1 = self.reverse(slow)
        while head and head1:
            if head.val != head1.val:
                return False
            head1 = head1.next
            head = head.next
        return True

    def reverse(self, head):
        """

        :param head:
        :return:
        """
        if not head or head.next:
            return head
        pre = head
        pre.next = None
        cur = head.next
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre
