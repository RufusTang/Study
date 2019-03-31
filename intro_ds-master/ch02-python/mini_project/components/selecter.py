# -*- coding: UTF-8 -*-
"""
此脚本用于得到出现次数最多的元素
"""


from mini_project.components.counter import wordCount


def getFrequentItem(data):
    """
    找出给定列表中，出现次数最多的元素

    参数
    ----
    data : list，原始数据列表

    返回
    ----
    re : list，在给定列表中出现次数最大的元素
    """
    _hash = wordCount(data)
    maxNum = max(_hash.values())
    # Python2和Python3的filter并不兼容，所以使用list(filter())
    return list(filter(lambda key: _hash[key] == maxNum, _hash))
