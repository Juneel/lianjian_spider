#!/usr/bin/env python3
# encoding: utf-8
"""
@version: 3.7
@author: lijun.03@bytedance.com
@file: main.py
@time: 2020/6/19 02:09
"""
from shanghai.spider import get_school_list_by_district

if __name__ == '__main__':
    get_school_list_by_district("pudong")
