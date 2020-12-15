#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 19.py
@time: 2020/12/13 12:41
@source: https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/
@desc: 19. 删除链表的倒数第N个节点
"""
# 思路，一个指针先跑n，然后两个一起+1往前跑，当快指针为None的时候，慢指针恰好指向倒数n
# 凡是用到前驱节点的地方，最好加个dummy节点
from list_node import ListNode


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        slow = head
        slow_pre = dummy
        fast = head
        while n > 0:
            fast = fast.next
            n -= 1
        while slow and fast:
            slow_pre = slow
            slow = slow.next
            fast = fast.next
        slow_pre.next = slow.next
        slow.next = None
        return dummy.next
