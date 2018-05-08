# -*- coding: utf-8 -*-
import os

from selenium import webdriver
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
import time
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower


class Creat_media(BasePage):

    #创建图文素材用例
    def creat_media(self):
        print self.printime(),u'开始执行图文素材创建用例'
        self.dominant_wait('x', '//*[@id="ul-nav-2"]/li[1]/a')  #点击素材管理菜单
        time.sleep(3)
        self.dominant_wait('x','//*[@id="con-graphic"]/div[1]/div[2]/div/a[2]') #点击新建图文按钮
        print self.printime(),u'点击新建图文按钮成功'
        self.find_element_input('x','//*[@id="exampleInputText1"]',u'自动化创建'+self.deprint())
        self.find_element_click('x','//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[4]/div[3]/div')
        pic=os.getcwd()
        # print pic
        os.system(pic +  "/upload.exe")
        time.sleep(3)
        self.find_element_input('x','//*[@id="con-local"]/section/section/div[2]/form/div[1]/div[6]/textarea',u'尤梅枝的摘要'+self.deprint())
        # self.find_element_click('x','.//*[@id="con-local"]/section/section[1]/div[2]/form/div[1]/div[9]/div[2]')
        self.find_element_input('x','//*[@id="exampleInputText2"]','http://www.baidu.com')
        self.find_element_click('x','//*[@id="con-local"]/section/section/div[2]/form/div[2]/button[1]')
        time.sleep(5)
        title=self.driver.find_element_by_xpath('//*[@id="dialogBox"]/div/div/div[2]/div/div').text
        self.find_element_click('x','//*[@id="dialogBox"]/div/div/div[3]/button[1]')
        # print title
        print self.printime(),u'图文素材创建用例执行完毕'
        return title
    #删除第一条图文素材用例
    def delete_media(self):
        print self.printime(),u'开始执行图文素材删除用例'
        self.dominant_wait('x', '//*[@id="ul-nav-2"]/li[1]/a')  # 点击素材管理菜单
        time.sleep(3)
        self.find_element_input('x','//*[@id="txtSearchGraphics"]/input',u'自动化')
        self.find_element_click('x','//*[@id="con-graphic"]/div[1]/div[1]/div/a')
        time.sleep(3)
        text=self.find_element_text('x','//*[@id="con-graphic"]/div[7]/div')
        print text
        #判断是否存在标题包含“自动化”的图文素材，如果查询结果返回暂无数据则跳过，否则删除第一条素材
        if text==u'暂无数据':
            pass
        else:
            self.dominant_wait('x', '//*[@id="con-graphic"]/div[2]/div[1]/div/div[3]/span/a[4]')
            time.sleep(3)
            self.dominant_wait('x', '//*[@id="dialogBox"]/div/div/div[3]/button[1]')

        print self.printime(), u'图文素材删除用例执行完毕'






if __name__ == '__main__':
    driver = brower()
    login= LoginPage(driver)
    login.login()
    chooseP = ChoosePage(driver)
    chooseP.click_menu_bt("1")
    test=Creat_media(driver)
    # title=test.creat_media()
    # time.sleep(3)
    # test = Creat_media(driver)
    # title = test.creat_media()
    test.delete_media()
