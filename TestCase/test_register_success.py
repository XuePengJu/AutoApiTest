#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/27 12:02 PM
# @Author : 夏见。
# @File : test_register_success.py

import logging
import unittest

from api.register import RegisterApi
from common import conf, utils
from common import getPhoneNumber


class TestRegisterSuccess(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.register_api = RegisterApi

    def test_register_success(self):
        # 测试数据
        mobile = getPhoneNumber.getPhoneNumber()
        pwd = conf.BSAE_PASSWORD
        type_int = conf.BASE_TYPEINT

        # 发送注册请求
        response = self.register_api.register(mobile, pwd, type_int)
        json_data = response.json()
        logging.info("response= {}".format(json_data))

        # 断言
        utils.common_assert(self, response, 200, 0, "OK")
        logging.info("注册成功用例执行完毕！")
