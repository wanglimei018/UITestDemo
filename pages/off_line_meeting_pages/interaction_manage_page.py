# -*- coding: utf-8 -*-

from pages.common_pages.base import BasePage
from pages.common_pages.driver import brower
import time
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.off_line_meeting_pages.index_page import IndexPage



class InteractionPageManage(BasePage):

    # 创建问卷
    def creat_questionnaire(self):
        time.sleep(5)
        self.deprint("开始创建问卷")
        """
        # 点击左侧的“互动环节”按钮
        self.driver.find_element_by_css_selector(
            "body > div.g-container > div.g-left.s-left > ul.m-nav-ul.nav-event.ng-scope > li:nth-child(6) > a > strong").click()
        self.driver.implicitly_wait(30)
        time.sleep(3)

        """
        self.driver.find_element_by_css_selector("#g-right > div > div.event-title.ng-scope > div > div > a").click()  # 点击“创建互动”按钮
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_css_selector(
            "#g-right > div > div.event-title.ng-scope > div > div > ul > li:nth-child(1) > a").click() # 点击下拉列表“创建问卷”选项

if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    o.click_menu_bt('9')
    o = IndexPage(dr)
    o.click_linelist()
    o = InteractionPageManage(dr)
    o.creat_questionnaire()




