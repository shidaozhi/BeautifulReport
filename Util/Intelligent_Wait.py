#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    # @ file   : Intelligent_Wait.py
    # @ Author : antony_shi
    # @ Create : 2021/8/30 10:18
    # @ Email  : antony_shi@163.com
    # @ Features : 用于实现智能等待页面元素的出现

"""
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as es
from selenium.webdriver.support.ui import WebDriverWait


class WaitUntil:

    def __init__(self, driver):
        self.locationTypeDict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "css_selector": By.CSS_SELECTOR,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 30)

    def presence_of_element_located(self, locationType, locatorExpression, *args):
        """
        显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
        """
        try:
            if locationType.lower() in self.locationTypeDict:
                self.wait.until(
                    es.presence_of_element_located((
                        self.locationTypeDict[locationType.lower()], locatorExpression)))
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    def clickable_of_element(self, locationType, locatorExpression, *args):
        """
        判断某个元素中是否可见并且是enable的，代表可点击
        """
        try:
            if locationType.lower() in self.locationTypeDict:
                self.wait.until(
                    es.element_to_be_clickable((
                        self.locationTypeDict[locationType.lower()], locatorExpression)))
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    def selection_of_element(self, locationType, locatorExpression, *args):
        """
        判断某个元素是否被选中了,一般用在下拉列表
        """
        try:
            if locationType.lower() in self.locationTypeDict:
                self.wait.until(
                    es.element_to_be_selected((
                        self.locationTypeDict[locationType.lower()], locatorExpression)))
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    def frame_to_be_available_and_switch_to_it(self, locationType, locatorExpression, *args):
        """
        检查frame是否存在，存在则切换进去
        """
        try:
            self.wait.until(
                es.frame_to_be_available_and_switch_to_it((
                    self.locationTypeDict[locationType.lower()], locatorExpression)))
        except Exception as e:
            # 抛出异常信息给上层调用者
            raise e

    def visibility_element_located(self, locationType, locatorExpression, *args):
        """
        显示等待页面元素的出现
        """
        try:
            element = self.wait.until(
                es.visibility_of_element_located((self.locationTypeDict[locationType.lower()], locatorExpression)))
            return element
        except Exception as e:
            raise e
