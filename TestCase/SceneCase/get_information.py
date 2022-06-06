#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/6/6 17:00
# @Author : 夏见。
# @File : get_information.py

import unittest

from TestCase.SingleCase.test_login_success import TestLoginSuccess
from TestCase.SingleCase.test_register_success import TestRegisterSuccess


class TestGetInForMation(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 先注册
        TestRegisterSuccess().test_register_success()
        # 在登录
        TestLoginSuccess().test_login_success()
#         在获取用户信息
# TODO 解决原接口直接调登录接口获取token的问题
