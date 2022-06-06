#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/27 11:57 PM
# @Author : 夏见。
# @File : test_login.py

import json
import logging
import unittest

from parameterized import parameterized

from api.login import LoginApi
from common import conf, utils


# 构造测试数据，读取JSON文件
def build_data():
    test_data = []
    with open(conf.BASE_DIR + "/data/login.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            mobile_phone = case_data.get("mobile_phone")
            pwd = case_data.get("pwd")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((mobile_phone, pwd, status_code, code, msg))
        # logging.info(" Test_data={}".format(test_data))
    return test_data


class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    # 登录
    @parameterized.expand(build_data)
    def test_login(self, mobile_phone, pwd, status_code, code, msg):
        logging.info("打印取到的参数化数据： {}，{}，{}，{}，{}".format(mobile_phone, pwd, status_code, code, msg))
        # 登录
        response = self.login_api.login(mobile_phone, pwd)
        logging.info("response= {}".format(response.json()))
        # 断言
        utils.common_assert(self, response, status_code, code, msg)
        # self.assertEqual(json_data["code"], datacode, "断言返回消息体的code码")
        # self.assertEqual(json_data["msg"], msg, "断言msg消息")
        logging.info("Login用例执行完毕 ***************************************************************************")
        # 保存token数据
        if response.json()["msg"] == "OK":
            token = response.json()["data"]["token_info"]["token"]
            conf.header_data["Authorization"] = "Bearer " + token
            logging.info(f"utils.header_data== {conf.header_data}")
            # app.a = 2
