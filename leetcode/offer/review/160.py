#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 160.py
@time: 2021/1/23 16:31
@source: https://leetcode-cn.com/problems/intersection-of-two-linked-lists/
@desc: 160. 相交链表
"""
# 思路1 暴力法，对于A的每一个元素，都检查是不是与B相交，时间复杂度 O(m+n)
# 思路2 哈希法，对于A中元素进行哈希，然后B进行检查，时间复杂度O(m+n)，空间O min(m, n)
# 思路3 先行法，算出A，B链的长度差值，然后长的那个先走差值步骤，再一起往后进行判断  ，时间复杂度O(m+n)*2
# 思路4 双指针法，指针P1，P2分别指向A，B，当到结尾的时候，P1指向P2，P2到结尾指向P1，两个继续向后，直到相等或者为空，时间复杂度为O(m+n)


class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1 = headA
        p2 = headB
        have_change_a = False
        have_change_b = False
        while p1 and p2:
            if p1 == p2:
                return p1
            p1 = p1.next
            p2 = p2.next
            if not p1 and not have_change_a:
                have_change_a = True
                p1 = headB
            if not p2 and not have_change_b:
                have_change_b = True
                p2 = headA
        return None
