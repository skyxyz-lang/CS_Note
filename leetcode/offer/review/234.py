#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 234.py
@time: 2021/1/23 16:57
@source: https://leetcode-cn.com/problems/palindrome-linked-list/
@desc: 234. 回文链表
"""
# 思路1：存到一个数组进行遍历，时间复杂度 O(n),空间复杂度O(n)
# 思路2：快慢指针找到中点所在，然后反转后半部分，再比遍历比较值,时间复杂度O(n)，空间复杂度O(1)


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return True
        slow = head
        fast = head
        pre = None
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None
        slow = self.reverse(slow)
        while slow and head:
            if slow.val != head.val:
                return False
            slow = slow.next
            head = head.next
        return True

    def reverse(self, head):
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