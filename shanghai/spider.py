#!/usr/bin/env python3
# encoding: utf-8
"""
@version: 3.7
@author: lijun.03@bytedance.com
@file: spider.py
@time: 2020/6/19 01:37
"""
from bs4 import BeautifulSoup
import requests
from shanghai.conf import *


def get_school_list_by_district(district_name):
    """
    get primary school list by district name
    :param district_name:
    :return: list
    """
    if district_name not in districts:
        return list()
    try:
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Cache-Control": "no-cache",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36"
        }
        plain_text = requests.get(url=SOUFANG_SHANGHAI_PUDONG_URL, headers=headers).text
        soup = BeautifulSoup(plain_text, features="html.parser")
    except ConnectionError:
        return list()
    housing_estate_list = soup.findAll('div', {'class': 'fanye gray6'})
    print(housing_estate_list)
    return housing_estate_list
