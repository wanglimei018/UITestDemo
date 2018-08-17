# -*- coding: utf-8 -*-

import time
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower


class SectionListPage(BasePage):

    # 点击新建栏目
    def new_section(self):
        try:
            self.deprint("开始点击新建栏目")
            time.sleep(3)
            # self.driver.switch_to.window(self.driver.window_handles[-1])  # 获取下一个窗口句柄
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[3]/div[2]/a')  # 点击新建栏目的按钮
            self.deprint("新建栏目按钮成功")
            self.find_element_input('x','//*[@id="manageArticleCategoryWindow"]/div[2]/div[1]/div/div/input',"automation")  #输入栏目名称
            #self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[2]/div[11]/div[8]/div/div/div[2]')  #点击“自动化行为标签”
            #self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[2]/div[11]/div[8]/div/div/div[3]/div[1]/span[1]')  #选择标签
            self.scrollbar("bottom")
            self.find_element_click('x','//*[@id="manageArticleCategoryWindow"]/div/div/div[3]/button[2]')  #点击保存按钮
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
            self.deprint("删除栏目失败")

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
            print browseNum,browseSum
            return browseNum,browseSum
        except:
            self.deprint("数据明细页面打开失败")

    # 点击“查看”按钮旁边的更多功能
    def choose_more(self):  # 20180817
        self.deprint("复制浏览链接")
        time.sleep(3)
        self.wait_is_visible('x',
                                '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/a')  # 点击第一行栏目的更多按钮

        self.wait_is_visible('x',
                                '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[5]/div/div/ul/li[2]/a')  # 点击获取链接按钮

        time.sleep(2)
        wap_url = self.find_element_AttributeText('x',
                                                  '//*[@id="copyArticleCategoryLinkWindow"]/div/div/div[2]/div/div/input',
                                                  "value")  # 得到浏览地址
        self.find_element_click('x', '//*[@id="copyArticleCategoryLinkWindow"]/div/div/div[3]/a[2]')  # 点击复制按钮
        return wap_url
        self.deprint("复制浏览链接成功")

    # 点击一个栏目
    def choose_firstsection(self):
        try:
            self.deprint("点击第一个栏目")
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[5]/table/tbody/tr[1]/td[3]/a')  # 点击第一个栏目按钮
        except:
            self.deprint("点击第一个栏目失败")

    # 点击新建文章按钮
    def create_button_article(self):
        try:
            self.deprint("点击新建文章按钮")
            time.sleep(3)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[4]/div[2]/a')  # 点击新建文章的按钮
        except:
            self.deprint("点击新建文章按钮失败")

    # 新建文章
    def create_article(self):
        now = int(time.time())
        timeArray = time.localtime(now)
        otherStyleTime = time.strftime("%Y--%m--%d %H:%M:%S", timeArray)
        self.element_value_input('x', '//*[@id="articleTitle"]', u'文章' + otherStyleTime)
        # self.element_click('x', '/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[6]/div/label[1]')
        self.element_click('x','/html/body/div[1]/div[1]/div[2]/div[2]/div[1]/div[3]/div[4]/div/label[1]/span')# 点击“分享设置”的“允许”
        self.scrollbar("100")
        time.sleep(2)
        self.wait_is_visible('x',
                             '/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/div/div[2]')  # 点击便签输入框，进行打标签
        self.wait_is_visible('x',
                             '/html/body/div[1]/div[1]/div[2]/div[2]/div[2]/div[3]/div/div/div/div/div[3]/div[1]/span[1]')  # 选择“1”的标签
        self.scrollbar("bottom")
        self.wait_is_visible('x', '/html/body/div[1]/div[1]/div[2]/div[1]/div[4]/div')  # 点击保存按钮
        self.wait_is_visible('x', '//*[@id="alertCommon"]/div/div/div[3]/button')  # 点击弹出弹框的“确定”按钮“
        time.sleep(2)






if __name__ == '__main__':
    dr = brower()
    object = LoginPage(dr)
    object.login()
    object = ChoosePage(dr)
    object.click_menu_bt('22')
    q=SectionListPage(dr)

    # q.choose_firstsection()
    # q.create_button_article()
    # q.create_article()


    q.new_section()
    # q.choose_more()
    # object.browse_section()
    # object.open_detail_data()
    # object.delete_section()