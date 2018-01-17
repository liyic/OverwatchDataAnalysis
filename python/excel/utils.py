# -*- coding:utf-8 -*-
"""
@Author: Komorebi
"""


def time_format(seconds):
    """
    格式化时间
    :param seconds: 秒
    :return: 时: 分: 秒
    """
    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%02d:%02d:%02d" % (h, m, s)


def capitalize(s):
    """
    将英雄名转换为首字母大写的形式
    :param s: str
    :return: Str
    """
    if s == 'dva':
        return 'D. Va'
    else:
        return None if s is None else s.capitalize()


def to_hex(array):
    b, g, r = array[0], array[1], array[2]
    if (int(r) + int(g) + int(b))/3 < 90:
        return 'F7F7F7'
    else:
        return (hex(r) + hex(g)[2:] + hex(b)[2:]).upper()[2:]