#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/27 10:50 PM
# @Author : 夏见。
# @File : login.py
import logging

import requests

from common import conf


class LoginApi:

    def __init__(self):
        # 登录URL
        self.login_url = conf.BASE_URL + "/member/login"
        logging.info(f"login_url: {self.login_url}")

        # 登录

    def login(self, mobile_phone, pwd):
        ruquest_data = None
        if mobile_phone is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["mobile_phone"] = mobile_phone
        if pwd is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["pwd"] = pwd

        header_data = conf.header_data
        logging.debug("开始请求登录接口ing")
        response = requests.post(self.login_url, json=ruquest_data, headers=header_data)
        logging.info(f"response= {response.json()}")
        return response


if __name__ == '__main__':
    from common.utils import init_log_config

    init_log_config()
    res = LoginApi().login(conf.base_user, conf.base_pass)
    # print("response= {}".format(res.json()))
    # mobile_id = res.json()["data"]["id"]
    # print("json()中括号 mobile_id=", mobile_id)
    # jsonData = res.json()
    # print("getResponse.data.id= ", jsonData.get("data").get("id"))
