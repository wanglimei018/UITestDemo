# -*- coding: utf-8 -*-

import time
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import selenium.webdriver.support.ui as ui
from selenium.webdriver.support.select import Select

class SectionListPage(BasePage):

    # 点击新建栏目
    def new_section(self):
        try:
            self.deprint("开始点击新建栏目")
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/a')  # 点击新建栏目的按钮
            self.deprint("新建栏目按钮成功")
            self.find_element_input('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[2]/div[1]/div/div/input',"automation")  #输入栏目名称
            #self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[2]/div[11]/div[8]/div/div/div[2]')  #点击“自动化行为标签”
            #self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[2]/div[11]/div[8]/div/div/div[3]/div[1]/span[1]')  #选择标签
            self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[3]/button[2]')  #点击保存按钮
        except:
            try:
                self.deprint("开始点击新建栏目")
                time.sleep(3)
                self.find_element_click('x', '/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/a')  # 点击新建栏目的按钮
                self.deprint("新建栏目按钮成功")
                self.find_element_input('x',
                                        '//*[@id="manageArticleCategoryWindow"]/div/div/div[2]/div[1]/div/div/input',
                                        "automation")  # 输入栏目名称
                #self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[2]/div[11]/div[8]/div/div/div[2]')  # 点击“自动化行为标签”
                #self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[2]/div[11]/div[8]/div/div/div[3]/div[1]/span[1]')  # 选择标签
                self.find_element_click('x', '//*[@id="manageArticleCategoryWindow"]/div/div/div[3]/button[2]')  # 点击保存按钮
            except:
                self.deprint("新建栏目失败")

    #删除第一行栏目
    def delete_section(self):
        try:
            self.deprint("开始点击删除栏目")
            time.sleep(3)
            self.find_element_click('x','/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  #点击第一行栏目的更多按钮
            self.find_element_click('x','/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/ul/li[5]/a')  #点击删除按钮
            time.sleep(1)
            self.find_element_click('x','//*[@id="alertCommon"]/div/div/div[3]/button[2]')  #点击确定按钮
            self.deprint("删除栏目成功")
        except:
            try:
                self.deprint("开始点击删除栏目")
                time.sleep(3)
                self.find_element_click('x',
                                     '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  # 点击第一行栏目的更多按钮
                self.find_element_click('x',
                                     '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/ul/li[5]/a')  # 点击删除按钮
                time.sleep(1)
                self.find_element_click('x', '//*[@id="alertCommon"]/div/div/div[3]/button[2]')  # 点击确定按钮
                self.deprint("删除栏目成功")
            except:
                self.deprint("删除栏目失败")

    #浏览栏目--文章管理用例1使用
    def browse_section(self):
        try:
            self.deprint("开始浏览栏目")
            time.sleep(3)
            self.find_element_click('x','/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  # 点击第一行栏目的更多按钮
            self.find_element_click('x','/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/ul/li[2]/a')  #点击获取链接按钮
            time.sleep(2)
            wap_url=self.find_element_AttributeText('x','//*[@id="copyArticleCategoryLinkWindow"]/div/div/div[2]/div/div/input',"value")  #得到浏览地址
            self.find_element_click('x','//*[@id="copyArticleCategoryLinkWindow"]/div/div/div[3]/a[2]')  #点击复制按钮
            self.deprint("复制栏目链接成功")
            current_handle=self.driver.current_window_handle
            all_handles=self.driver.window_handles
            url=wap_url.encode('unicode-escape').decode('string_escape')
            newwindow = 'window.open("'+url+'")'
            self.driver.execute_script(newwindow)
            self.deprint("完成浏览栏目")
            time.sleep(3)
            #self.driver.close()
            for handle in all_handles:
                if handle==current_handle:
                    self.driver.switch_to_window(handle)
            # self.driver.switch_to_window(self.driver.window_handles[1])
        except:
            try:
                self.deprint("开始浏览栏目")
                time.sleep(3)
                self.find_element_click('x',
                                     '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  # 点击第一行栏目的更多按钮
                self.find_element_click('x',
                                     '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/ul/li[2]/a')  # 点击获取链接按钮
                time.sleep(2)
                wap_url = self.find_element_AttributeText('x',
                                                          '//*[@id="copyArticleCategoryLinkWindow"]/div/div/div[2]/div/div/input',
                                                          "value")  # 得到浏览地址
                self.find_element_click('x', '//*[@id="copyArticleCategoryLinkWindow"]/div/div/div[3]/a[2]')  # 点击复制按钮
                self.deprint("复制栏目链接成功")
                current_handle = self.driver.current_window_handle
                all_handles = self.driver.window_handles
                url = wap_url.encode('unicode-escape').decode('string_escape')
                newwindow = 'window.open("' + url + '")'
                self.driver.execute_script(newwindow)
                self.deprint("完成浏览栏目")
                time.sleep(3)
                # self.driver.close()
                for handle in all_handles:
                    if handle == current_handle:
                        self.driver.switch_to_window(handle)
                # self.driver.switch_to_window(self.driver.window_handles[1])
            except:
                self.deprint("浏览栏目失败")

    #打开数据明细
    def open_detail_data(self):
        try:
            time.sleep(3)
            self.wait_is_visible('x','/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  # 点击第一行栏目的更多按钮
            time.sleep(1)
            self.wait_is_visible('x','/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/ul/li[3]/a')  # 点击数据明细按钮
            self.deprint("打开数据明细页面成功")
            browseNum=self.find_element_text('x','/html/body/div[1]/div[1]/div[3]/div/div[3]/div[1]/div/div/span[1]')  #抓取浏览量
            browseSum=self.find_element_text('x','/html/body/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div/span[1]')  #抓取浏览人数
            self.find_element_click('x','/html/body/div[1]/div[1]/div[1]/nav/a[2]')  #返回栏目列表
            return browseNum,browseSum
        except:
            try:
                time.sleep(3)
                self.find_element_click('x',
                                     '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  # 点击第一行栏目的更多按钮
                self.find_element_click('x',
                                     '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/ul/li[3]/a')  # 点击数据明细按钮
                self.deprint("打开数据明细页面成功")
                browseNum = self.find_element_text('x',
                                                   '/html/body/div[1]/div[1]/div[3]/div/div[3]/div[1]/div/div/span[1]')  # 抓取浏览量
                browseSum = self.find_element_text('x',
                                                   '/html/body/div[1]/div[1]/div[3]/div/div[3]/div[2]/div/div/span[1]')  # 抓取浏览人数
                self.find_element_click('x', '/html/body/div[1]/div[1]/div[1]/nav/a[2]')  # 返回栏目列表
                return browseNum, browseSum
            except:
                self.deprint("数据明细页面打开失败")


if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()
    object = ChoosePage(dr)
    object.click_menu_bt('21')
    object=SectionListPage(dr)
    object.new_section()
    object.browse_section()
    object.open_detail_data()
    object.delete_section()