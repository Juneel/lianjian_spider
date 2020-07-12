#!/usr/bin/env python3
# encoding: utf-8
"""
@version: 3.7
@author: lijun.03@bytedance.com
@file: __init__.py
@time: 2020/6/19 01:24
"""


class City:
    def __init__(self):
        self.city_code = None
        self.city_name = None


class District:
    def __init__(self):
        self.city_code = None
        self.district_code = None
        self.district_name = None


class HousingEstate:
    def __init__(self):
        self.city_code = None
        self.district_code = None
        self.housing_estate_name = None
