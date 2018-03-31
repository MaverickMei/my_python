#!/usr/bin/env python 
# -*- coding: utf-8 -*-
import requests
import json
from prettytable import PrettyTable

if __name__ == '__main__':

    url = 'https://data-gkcx.eol.cn/soudaxue/queryProvince.html'

    row = PrettyTable()
    row.field_names = ["地区", "年份", "考生类别", "批次", "分数线"]

    for i in range(1, 3):
        data = {"messtype": "json",
                "page": i,
                "size": 50,
                "callback":
                    "jQuery1830426658582613074_1469201131959",
                "_": "1469201133189",
                }
        school_datas = requests.post(url, data=data).json()
        datas = school_datas["school"]
        for data in datas:
            row.add_row((data["province"], data["year"], data["bath"], data["type"], data["score"]))

    print(row)