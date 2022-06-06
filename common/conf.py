#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/2 6:36 PM
# @Author : 夏见。
# @File : conf.py

# 项目根目录
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# 项目基本路径
BASE_URL = "http://api.mypeng.site:8080/futureloan"

# base_user = "13800000001"
base_user = "13800000002"
base_pass = "1234567@"
BASE_TYPEINT = 1
# 请求头数据
header_data = {
    "Content-Type": "application/json",
    "X-Lemonban-Media-Type": "lemonban.v2"
}
