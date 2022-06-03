#!/usr/bin/python3
# -*- coding:utf-8 -*-

"""
    # @ file   : Clipboard_Simulation.py
    # @ Author : antony_shi
    # @ Create : 2021/8/30 10:18
    # @ Email  : antony_shi@163.com
    # @ Features : 用于实现将数据设置到剪切板中

"""
import win32clipboard as wc
import win32con


class SimulateClipboard:
    # 读取剪切板
    @staticmethod
    def get_clipboard():
        # 打开剪切板
        wc.OpenClipboard()
        # 获取剪切板中的数据
        data = wc.GetClipboardData(win32con.CF_TEXT)
        # 关闭剪切板
        wc.CloseClipboard()
        # 返回剪切板数据给调用者
        return data

    # 设置剪切板内容
    @staticmethod
    def set_clipboard(content):
        # 打开剪切板
        wc.OpenClipboard()
        # 清空剪切板
        wc.EmptyClipboard()
        # 将数据a string写入剪切板
        wc.SetClipboardData(win32con.CF_UNICODETEXT, content)
        # 关闭剪切板
        wc.CloseClipboard()


if __name__ == '__main__':
    # 设置剪切板内容
    SimulateClipboard.set_clipboard("set content into clipboard")
    # 获取剪切板内容并赋给str
    str = SimulateClipboard.get_clipboard()
    print(str)
