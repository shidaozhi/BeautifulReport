# -*- coding: utf-8 -*-
"""
@author: Antony

@software: pycharm

@file:  test_baidu.py

@time: 2020/7/26 0026 21:33

@Desc:

"""

import os
import unittest

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By

from BeautifulReport.BeautifulReport import BeautifulReport


class TestBaidu(unittest.TestCase):
    """测试报告"""
    __author__ = 'Antony'
    dr = None
    if not os.path.exists('img'):
        os.makedirs('img')
    img_path = r'img'

    @staticmethod
    def parse(html, xpath):
        """
                    解析页面中的元素并返回一个对象
                :param xpath: 需要获取页面中的元素对应的xpath
                :param html: 页面的html元素
                :return:
                """
        return etree.HTML(html).xpath(xpath)

    def save_img(self, img_name):
        """
                  传入一个img_name, 并存储到默认的文件路径下
              :param img_name:
              :return:
              """
        self.dr.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))
        print("图片存放路径：{}".format(os.path.abspath(self.img_path)))

    @classmethod
    def setUpClass(cls) -> None:
        cls.dr = webdriver.Chrome()
        cls.url = 'https://www.baidu.com'

    @classmethod
    def tearDownClass(cls) -> None:
        cls.dr.close()

    def test_baidu_index(self):
        """
        测试访问首页正常, 并使用title进行断言
        """
        self.dr.get(self.url)
        print('打开浏览器, 访问: {}'.format(self.url))
        title = TestBaidu.parse(self.dr.page_source, '//title/text()')[0]
        print("获取对应的title: {}".format(title))
        self.assertEqual(title, "百度一下，你就知道")

    # 测试之前->截图,测试之后->截图
    @BeautifulReport.add_test_img('百度首页访问截图', '点击按钮后截图')
    def test_save_img(self):
        """
        打开首页, 截图, 在截图后点击第一篇文章连接, 跳转页面完成后再次截图
        """
        self.dr.get(self.url)
        self.save_img('百度首页访问截图')
        self.dr.find_element(By.ID, 'su').click()
        self.save_img('点击按钮后截图')
        title = TestBaidu.parse(self.dr.page_source, '//title/text()')[0]
        self.assertEqual(title, '百度一下，你就知道')

    # 测试出错->截图，名称与方法名一致
    @BeautifulReport.add_test_img('test_errors_save_img')
    def test_errors_save_img(self):
        """
                  如果在测试过程中, 出现不确定的错误, 程序会自动截图, 并返回失败, 如果你需要程序自动截图, 则需要咋测试类中定义 save_img方法
              """
        self.dr.get(self.url)
        self.dr.find_element(By.ID, 'kw22').send_keys('selenium')

    # 测试成功->截图,名称与方法名一致
    @BeautifulReport.add_test_img('test_success_case_img')
    def test_success_case_img(self):
        """
                   如果case没有出现错误, 即使使用了错误截图装饰器, 也不会影响case的使用
        """
        self.dr.get(self.url)
        self.dr.find_element(By.XPATH, '//title/text()')
        # title = TestBaidu.parse(self.dr.page_source, '//title/text()')[0]
        # print(title)
