#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/27 11:59 PM
# @Author : 夏见。
# @File : test_register.py

import json
import logging
import unittest

from parameterized import parameterized

from api.register import RegisterApi
from common import conf
from common import dbUtil, utils


def build_data():
    test_data = []
    with open(conf.BASE_DIR + "/data/register.json", encoding="UTF-8") as f:
        json_data = json.load(f)
        for case_data in json_data:
            # mobile_phone = getPhoneNumber.getPhoneNumber()  # 获取一个手机号
            mobile_phone = case_data.get("mobile_phone")
            pwd = case_data.get("pwd")
            type_int = case_data.get("type_int")
            reg_name = case_data.get("reg_name")
            status_code = case_data.get("status_code")
            code = case_data.get("code")
            msg = case_data.get("msg")
            test_data.append((mobile_phone, pwd, type_int, reg_name, status_code, code, msg))
        logging.info(f"test_data={test_data}")
    return test_data


class TestRegister(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.register_api = RegisterApi

    def setUp(self) -> None:
        pass

    # 取参数化配置注册
    @parameterized.expand(build_data)
    def test_register(self, mobile_phone, pwd, type_int, reg_name, status_code, code, msg):
        db = dbUtil.DBUtil('root', 'Lemon123456!', 'api.mypeng.site', 3305, 'futureloan')
        delete_sql: str = f"DELETE FROM member WHERE mobile_phone = {mobile_phone}"
        if mobile_phone:
            db.write_db(delete_sql)
        # 注册
        response = self.register_api.register(mobile_phone, pwd, type_int, reg_name)
        logging.info(f"response= {response.json()}")
        # 断言
        utils.common_assert(self, response, status_code, code, msg)
