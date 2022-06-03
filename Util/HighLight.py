# -*- coding: utf-8 -*-

"""
    # @ file : HighLight.py
    # @ Author : antony_shi
    # @ Create : 2021/9/21 8:22
    # @ Email : antony_shi@163.com
    # @ Features : https://www.cnblogs.com/milesma/p/12333841.html

"""


class HighLight:
    def __init__(self, driver):
        self.driver = driver

    def highlight_element(self, element):
        """
        调用JS，用于高亮控件
        :param element:
        :return:
        """
        self.driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element,
                                   "background: yellow; border:2px solid red;")
