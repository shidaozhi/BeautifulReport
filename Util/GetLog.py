#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    # @ file   : GetLog.py
    # @ Author : antony_shi
    # @ Create : 2021/8/30 10:18
    # @ Email  : antony_shi@163.com
    # @ Features : 记录日志

"""
import logging
import time


class Logger:

    def __init__(self, logger):
        """
        指定保存日志的文件路径，日志级别，以及调用文件
            将日志存入到指定的文件中
        :param logger:
        """
        # 创建一个logger
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.DEBUG)

        # 创建一个handler，用于写入日志文件
        rq = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))
        log_path = "\\TestResult\\TestLog\\"
        print(log_path)
        log_name = log_path + rq + '.log'
        file_handler = logging.FileHandler(log_name)
        file_handler.setLevel(logging.INFO)

        # 再创建一个handler，用于输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)

        # 定义handler的输出格式
        formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 给logger添加handler
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def get_log(self):
        return self.logger
