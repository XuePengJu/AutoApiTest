#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/5/1 12:12 PM
# @Author : 夏见。
# @File : get_env.py

import configparser
import logging
import os

import utils


def get_env(env, sections, parameter):  # todo 真实项目都有环境变量都有一个环境变量名称。根据环境变量来区分使用哪个配置文件
    osdir = utils.BASE_DIR + "/env"
    # 在当前文件路径下查找.ini文件
    if env == "test":
        config_path = os.path.join(osdir, "test.ini")
        logging.info(f"config_path= {config_path}")
    elif env == "pre":
        config_path = os.path.join(osdir, "pre.ini")
        logging.info(f"config_path= {config_path}")
    else:
        config_path = os.path.join(osdir, "local.ini")
        logging.info(f"config_path= {config_path}")
    conf = configparser.ConfigParser()
    # 读取.ini文件
    conf.read(config_path)

    # get()函数读取参数值,
    '''
    所有的section名称都是独占一行，并且sections名字都被方括号包围着（[ and ])。在section声明后的所有parameters都是属于该section
    每一个parameter都有一个name和一个value，name和value是由等号“=”隔开
    '''
    result: str = conf.get(sections, parameter)
    # name = conf.get("BaseUrl", "base_url")
    logging.info(f"result= {result}")
    return result

    # print(conf.sections())  # 获取所有的标题
    # print(conf.options('section1'))  # 获取键
    # print(conf.items('BaseUrl'))  # 获取键值对


if __name__ == '__main__':
    from common.utils import init_log_config

    init_log_config()
    get_env("local", "db", "server")
    get_env("local", "db", "port")
    # test = os.environ['env']
    # print(test)

    # 使用os.environ获取环境变量字典，environ是在os.py中定义的一个dict environ = {}
    # env_dist = os.environ
    #
    # # 打印所有环境变量，遍历字典
    # for key in env_dist:
    #     print(key + ' : ' + env_dist[key])
