#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/27 11:58 PM
# @Author : 夏见。
# @File : test_login_success.py

import logging
import unittest

from api.login import LoginApi
from common import conf, utils


class TestLoginSuccess(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    # 登录成功
    def test_login_success(self):
        # 测试数据
        mobile = "13800000002"
        pwd = "1234567@"

        # 登录
        response = self.login_api.login(mobile, pwd)
        logging.info(f"response= {response.json()}")

        # 断言
        utils.common_assert(self, response, 200, 0, "OK")

        # 保存token数据
        token = response.json()["data"]["token_info"]["token"]
        conf.header_data["Authorization"] = "Bearer " + token
        logging.info(f"utils.header_data== {conf.header_data}")
