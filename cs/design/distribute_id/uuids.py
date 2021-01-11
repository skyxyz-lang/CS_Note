#!/usr/bin/env python
# encoding: utf-8
"""
@author: skyxyz-lang
@file: uuids.py
@time: 2021/1/10 19:57
@source:
@desc:
# uuid是指Universally Unique Identifier，翻译为中文是通用唯一识别码，UUID 的目的是让分布式系统中的所有元素都能有唯一的识别信息
uuid
位数为 32 个 16 进制的数字，所有其位数为 32 * 4 = 128 位
其分割形式为 8-4-4-4-12
xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx
数字 M的四位表示 UUID 版本，当前规范有5个版本，M可选值为1, 2, 3, 4, 5 ；
数字 N的一至四个最高有效位表示 UUID 变体( variant )，有固定的两位10xx因此只可能取值8, 9, a, b
version 1, date-time & MAC address
version 2, date-time & group/user id
version 3, MD5 hash & namespace
version 4, pseudo-random number
version 5, SHA-1 hash & namespace
"""



