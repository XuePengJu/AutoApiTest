#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2022/4/29 3:57 PM
# @Author : 夏见。
# @File : getPhoneNumber.py

import random
import time


def getPhoneNumber():
    # 第二位数字
    second = [3, 5, 8][random.randint(0, 2)]

    # 第三位数字
    third = [2, 3, 5, 7, 8, 9][random.randint(0, 5)]

    # 最后八位数字
    suffix = str(int(time.time()))[2::]

    # 拼接手机号
    return "1{}{}{}".format(second, third, suffix)


if __name__ == '__main__':
    phone = getPhoneNumber()
    print(phone)
