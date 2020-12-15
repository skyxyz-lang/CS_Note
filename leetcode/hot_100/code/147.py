#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 147.py
@time: 2020/12/13 11:29
@source: https://leetcode-cn.com/problems/insertion-sort-list/
@desc: 147. 对链表进行插入排序
"""


class Solution(object):
    """

    """
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        cur = head.next
        head.next = None
        while cur:
            search_cur = head
            pre = None
            tmp = cur
            cur = cur.next
            tmp.next = None
            while search_cur and tmp and search_cur.val < tmp.val:
                pre = search_cur
                search_cur = search_cur.next
            if not pre:
                tmp.next = head
                head = tmp
            elif search_cur:
                pre.next = tmp
                tmp.next = search_cur
            else:
                pre.next = tmp
        return head
