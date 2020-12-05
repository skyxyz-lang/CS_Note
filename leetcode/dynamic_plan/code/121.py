#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: 121.py
@time: 2020/12/5 16:44
@source: https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/
@desc: 121. 买卖股票的最佳时机
"""


class Solution(object):
    """

    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        cur_min_price = float('inf')
        max_profit = 0
        for price in prices:
            if price < cur_min_price:
                cur_min_price = price
            if (price - cur_min_price) > max_profit:
                max_profit = price - cur_min_price
        return max_profit

