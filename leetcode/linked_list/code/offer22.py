#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: offer22.py
@time: 2020/12/9 22:50
@source:https://leetcode-cn.com/problems/lian-biao-zhong-dao-shu-di-kge-jie-dian-lcof/
@desc:剑指 Offer 22. 链表中倒数第k个节点
"""
from list_node import ListNode


class Solution(object):
    """

    """
    def getKthFromEnd(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        if k > length:
            return head
        gap = length - k
        while head and gap > 0:
            head = head.next
            gap -= 1
        return head


if __name__ == '__main__':
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    obj = Solution()
    head = obj.getKthFromEnd(a, 2)
    print head.val




