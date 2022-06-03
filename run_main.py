# -*- coding: utf-8 -*-
"""
    @author: Antony
    @software: pycharm
    @file:  run_main.py
    @time: 2020/7/26 0026 21:33
    @Desc:
"""
# __author__ = 'Leo'

import os
import sys
import time
import unittest

from BeautifulReport.BeautifulReport import BeautifulReport

sys.stdout.flush()

if not os.path.exists('report'):
    os.makedirs('report')


def add_case(case_path='./test_case', rule="test*.py"):
    """加载所有的测试用例"""

    discover = unittest.defaultTestLoader.discover(case_path, pattern=rule, top_level_dir=None)
    return discover


def run_case(test_suite):
    t1 = time.time()
    result = BeautifulReport(test_suite)
    # result.report(filename='测试报告', description='访问百度', report_dir='./report')
    result.report(filename='测试报告', description='测试deafult报告', report_dir='report', theme='theme_default')
    t2 = time.time()
    print("运行时间:%s" % (t2 - t1))


if __name__ == '__main__':
    cases = add_case()
    run_case(cases)
