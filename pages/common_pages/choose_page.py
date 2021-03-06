# -*- coding: utf-8 -*-
import time
from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower
from pages.common_pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChoosePage(BasePage):


    def click_menu_bt(self, button_pos):

        time.sleep(3)
        handleNow = self.driver.current_window_handle # 获得当前窗口
        self.driver.switch_to_window(handleNow)
        self.driver.implicitly_wait(30)
        css_path = "#sortContainer > a:nth-child(" + str(button_pos) + ")" #把按钮位置设为参数获取
        if button_pos =='1':
            self.deprint("开始进入微信")
        if button_pos =='8':
            self.deprint("开始进入线上会")
        if button_pos == '9':
            self.deprint("开始进入线下会")
        if button_pos == '11':
            self.deprint("开始进入问卷")
        if button_pos == '16':
            self.deprint("开始进入客户管理")
        if button_pos == '21':
            self.deprint("开始进入文章管理")
        self.wait_is_visible('css',css_path)
        self.driver.switch_to.window(self.driver.window_handles[-1]) # 获取下一个窗口句柄，跳转

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    # o.quit()