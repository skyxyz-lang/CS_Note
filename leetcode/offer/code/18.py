#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 18.py
@time: 2021/1/17 18:45
@source: https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/
@desc: 剑指 Offer 18. 删除链表的节点
"""
# 思路，遍历的时候保存前置节点，然后删除


class Solution(object):
    def deleteNode(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        pre = None
        current = head
        while current:
            if current.val == val:
                break
            pre = current
            current = current.next
        if not pre:
            return head.next
        else:
            pre.next = pre.next.next
        return head
