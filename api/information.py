#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/30 11:59 PM
# @Author : 夏见。
# @File : information.py
import logging

import requests

from api import login
from common import conf


class InForMation:

    def __init__(self):
        self.info_url = None

    def _get_member_id(self, mobile_phone, pwd):
        # 请求登录接口获取member_id
        response = login.LoginApi().login(mobile_phone, pwd)
        member_id = response.json()["data"]["id"]

        self.info_url = conf.BASE_URL + "/member/{}/info".format(member_id)
        logging.info(f"info_url: {self.info_url}")
        # 保存token数据
        token = response.json()["data"]["token_info"]["token"]
        conf.header_data["Authorization"] = "Bearer " + token
        logging.info(f"conf.header_data== {conf.header_data}")
        return member_id

    # 获取个人信息
    def get_information(self, mobile_phone, pwd):
        member_id = InForMation()._get_member_id(mobile_phone, pwd)
        self.info_url = conf.BASE_URL + f"/member/{member_id}/info"
        logging.info(f"info_url: {self.info_url}")
        header_data = conf.header_data
        logging.debug("开始请求获取个人信息接口ing")
        response = requests.get(self.info_url, headers=header_data)
        logging.info(f"response= {response.json()}")
        return response


if __name__ == '__main__':
    from common.utils import init_log_config

    init_log_config()
    InForMation().get_information("15851136191", "1234567@")
