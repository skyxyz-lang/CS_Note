#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 148.py
@time: 2020/12/13 11:24
@source: https://leetcode-cn.com/problems/sort-list/
@desc: 148. 排序链表
归并排序 O(nlogn)
"""


class ListNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution(object):
    """

    """
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        right_node = slow.next
        slow.next = None
        left = self.sortList(head)
        right = self.sortList(right_node)
        return self.merge(left, right)

    def merge(self, left, right):
        """

        :param left:
        :param right:
        :return:
        """
        head = ListNode(0)
        cur = head
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        while left:
            cur.next = left
            left = left.next
            cur = cur.next
        while right:
            cur.next = right
            right = right.next
            cur = cur.next
        return head.next


if __name__ == '__main__':
    a = ListNode(4)
    b = ListNode(2)
    c = ListNode(1)
    d = ListNode(3)
    a.next = b
    b.next = c
    c.next = d
    obj = Solution()
    res = obj.sortList(a)
    while res:
        print res.val
        res = res.next

