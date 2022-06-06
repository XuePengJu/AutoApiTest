#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/24 3:57 PM
# @Author : 夏见。
# @File : utils.py

import logging
import logging.handlers
import time

# 初始化日志配置
from common.conf import BASE_DIR


def init_log_config():
    # 创建日志器
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # 创建处理器（控制台、文件处理器）
    sh = logging.StreamHandler()
    log_file = BASE_DIR + "/log/futureloan_{}.log".format(time.strftime('%Y_%m_%d_%H', time.localtime()))
    # log_file = "./log/futureloan_{}.log".format(time.strftime('%Y_%m_%d_%H', time.localtime()))
    fh = logging.handlers.TimedRotatingFileHandler(log_file, when="midnight", interval=1,
                                                   backupCount=7, encoding="UTF-8")
    # 创建格式化器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    formatter = logging.Formatter(fmt)

    # 把格式化器添加到处理器
    sh.setFormatter(formatter)
    fh.setFormatter(formatter)

    # 把处理器添加到日志器中
    logger.addHandler(sh)
    logger.addHandler(fh)


# 通用断言方法
def common_assert(test_case, response, status_code, code, msg):
    test_case.assertEqual(status_code, response.status_code)
    logging.info("status_code断言完毕,预期：{},实际结果：{}".format(status_code, response.status_code))
    test_case.assertEqual(code, response.json().get("code"))
    logging.info("字段code断言完毕,预期：{},实际结果：{}".format(code, response.json().get("code")))
    test_case.assertIn(msg, response.json().get("msg"))
    logging.info("字段msg断言完毕,预期：{},实际结果：{}".format(msg, response.json().get("msg")))


if __name__ == '__main__':
    init_log_config()
    logging.info("test io")
