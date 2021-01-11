#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: snow_flake.py
@time: 2021/1/10 16:43
@source:
@desc: 分布式唯一ID雪花算法,雪花算法的原理
【1位】 【41位 时间戳】 【10位 机器码】 【12位 序列号】  = 64  mysql bigint 长度
优点：
1、分布唯一
2、高性能
3、趋势递增
4、长度较短
"""

import time


class SnowFlake(object):
    """
    雪花算法
    """
    def __init__(self, datacenter_id, work_id, sequence):
        """

        """
        # 64 位的划分
        self.work_id_bits = 5
        self.datacenter_id_bits = 5
        self.sequence_bits = 12
        # 最大值
        self.max_work_id = -1 ^ (-1 << self.work_id_bits)
        self.max_datacenter_id = -1 ^ (-1 << self.datacenter_id_bits)
        # 位偏移量
        self.work_id_shift = self.sequence_bits
        self.datacenter_id_shift = self.sequence_bits + self.work_id_bits
        self.timestamp_shift = self.sequence_bits + self.work_id_bits + self.datacenter_id_bits
        # 序列号掩码
        self.sequence_mask = -1 ^ (-1 << self.sequence_bits)

        self.datacenter_id = 0
        self.work_id = 0
        self.sequence = 0
        # 上次计算的时间戳
        self.last_timestamp = -1

        self.start_time = 1610272776000

        self.init(datacenter_id, work_id, sequence)

    def init(self, datacenter_id, work_id, sequence):
        """

        :param datacenter_id:
        :param work_id:
        :param sequence:
        :return:
        """
        if work_id > self.max_work_id or work_id < 0:
            raise ValueError("work_id error")
        if datacenter_id > self.max_datacenter_id or datacenter_id < 0:
            raise ValueError("datacenter_id error")
        self.work_id = work_id
        self.datacenter_id = datacenter_id
        self.sequence = sequence

    def get_mill_timestamp(self):
        """
        获取毫秒时间戳
        :return:
        """
        return int(time.time() * 1000)

    def till_next_mills(self, last_timestamp):
        """

        :param last_timestamp:
        :return:
        """
        timestamp = self.get_mill_timestamp()
        if timestamp <= self.last_timestamp:
            timestamp = self.get_mill_timestamp()
        return timestamp

    def get_distribute_id(self):
        """
        获取分布式ID
        :return:
        """
        time_stamp = self.get_mill_timestamp()
        if time_stamp < self.last_timestamp:
            raise ValueError("time error")
        if time_stamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & self.sequence_mask
            # 当前毫秒时间戳用完
            if self.sequence == 0:
                time_stamp = self.till_next_mills(self.last_timestamp)
        else:
            self.sequence = 0
        self.last_timestamp = time_stamp
        new_id = ((time_stamp - self.start_time) << self.timestamp_shift) | \
                 (self.datacenter_id << self.datacenter_id_shift) | (self.work_id << self.work_id_shift) | self.sequence
        return new_id


if __name__ == '__main__':
    obj = SnowFlake(10, 2, 0)
    for i in range(1000):
        print obj.get_distribute_id()

