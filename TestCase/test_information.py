#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/2 19:02 AM
# @Author : 夏见。
# @File : test_information.py

import logging
import unittest

from api.information import InForMation
from common import conf, utils


class TestInForMation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.mobile = conf.base_user
        cls.pwd = conf.base_pass
        cls.information_api = InForMation()

    def test_information(self):
        # 发送获取个人信息请求
        response = self.information_api.get_information(self.mobile, self.pwd)
        json_data = response.json()
        logging.info("response= {}".format(json_data))
        # 断言
        utils.common_assert(self, response, 200, 0, "OK")
        self.assertTrue(json_data["data"])
        logging.info("获取用户信息用例执行完毕！")
