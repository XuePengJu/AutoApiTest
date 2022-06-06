#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/27 10:55 PM
# @Author : 夏见。
# @File : register.py

import logging

from requests import request

from common import conf, getPhoneNumber


class RegisterApi:
    # 注册
    @staticmethod
    def register(mobile_phone, pwd, type_int, reg_name="AutoTestPy"):
        # 注册URL
        login_url = conf.BASE_URL + "/member/register"
        ruquest_data = None
        if mobile_phone is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["mobile_phone"] = mobile_phone
        if pwd is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["pwd"] = pwd
        if type_int is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["type"] = type_int
        if reg_name is not None:
            if ruquest_data is None:
                ruquest_data = {}
            ruquest_data["reg_name"] = reg_name

        logging.debug("request= {}".format(ruquest_data))
        logging.info("开始请求注册接口 ing ")
        return request('post', login_url, json=ruquest_data, headers=conf.header_data)


if __name__ == '__main__':
    # 拼接手机号
    phone = getPhoneNumber.getPhoneNumber()
    password = conf.BSAE_PASSWORD
    type_int = conf.BASE_TYPEINT
    response = RegisterApi.register(phone, password, type_int)
    logging.info("response= {}".format(response.json()))
