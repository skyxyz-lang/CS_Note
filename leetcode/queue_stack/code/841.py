#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 841.py
@time: 2020/11/22 22:22
@source:https://leetcode-cn.com/problems/keys-and-rooms/
@desc:841. 钥匙和房间
"""
import collections


class Solution(object):
    """

    """
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        if not rooms:
            return False
        queue = collections.deque()
        for k in rooms[0]:
            queue.append(k)
        rooms[0] = True
        while len(queue) > 0:
            key = queue.popleft()
            if rooms[key] is True:
                continue
            else:
                for k in rooms[key]:
                    queue.append(k)
                rooms[key] = True
        for tag in rooms:
            if tag is not True:
                return False
        return True
