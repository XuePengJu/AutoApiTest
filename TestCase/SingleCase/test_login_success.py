#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/27 11:58 PM
# @Author : 夏见。
# @File : test_login_success.py

import logging
import os
import unittest

from api.login import LoginApi
from common import conf, utils


class TestLoginSuccess(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()
        cls.pwd = conf.BSAE_PASSWORD
        # 先从环境变量中取值，找不到从配置文件中获取
        cls.mobile = os.getenv('BASE_MOBILE_PHONE')
        # BASE_MOBILE_ID = os.getenv('BASE_MOBILE_ID')
        if cls.mobile is None:
            # 测试数据
            cls.mobile = conf.BASE_MOBILE_PHONE

    # 登录成功
    def test_login_success(self):
        # 登录
        response = self.login_api.login(self.mobile, self.pwd)
        logging.info(f"response= {response.json()}")

        # 断言
        utils.common_assert(self, response, 200, 0, "OK")

        # 保存token数据
        token = response.json()["data"]["token_info"]["token"]
        conf.header_data["Authorization"] = "Bearer " + token
        logging.info(f"utils.header_data== {conf.header_data}")
