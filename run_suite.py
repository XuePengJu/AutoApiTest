import logging
import time
import unittest

from TestCase.test_login import TestLogin
from TestCase.test_login_success import TestLoginSuccess
from TestCase.test_register import TestRegister
from TestCase.test_register_success import TestRegisterSuccess
from TestCase.test_repeat_register import TestRepeatRegister
from common import utils
from tools.HTMLTestRunner import HTMLTestRunner

suite = unittest.TestSuite()

suite.addTest(unittest.makeSuite(TestLoginSuccess))
suite.addTest(unittest.makeSuite(TestRegisterSuccess))
suite.addTest(unittest.makeSuite(TestRepeatRegister))
suite.addTest(unittest.makeSuite(TestLogin))
suite.addTest(unittest.makeSuite(TestRegister))

# unittest.TextTestRunner().run(suite)

report_file = utils.BASE_DIR + "/report/report{}.html".format(time.strftime('%Y_%m_%d_%H', time.localtime()))
# print(report_file)

with open(report_file, "w") as f:
    runner = HTMLTestRunner(f, title="API接口自动化测试报告", description="futureloan项目接口自动化测试报告")
    runner.run(suite)

logging.info("用例执行完毕！！！！！！")
