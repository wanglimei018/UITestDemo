# -*- coding:utf-8 -*-
from pages.common_pages.driver import brower
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.webinar_pages.index_page import Webinar_IndexPage
import time

class Get_Guestnum(BasePage):

    def get_num(self):
        try:
            # time.sleep(5)
            self.wait_is_visible('x', '/html/body/div[1]/div[1]/ul/li[3]/h2/a')
            time.sleep(3)
            strguestnum = self.find_element_text('x', '/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/span')
            # 判断嘉宾的统计数字是否显示
            s = len(strguestnum[3:-4])
            if s == 0:
                time.sleep(2)
                strguestnum = self.find_element_text('x', '/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/span')
            num = strguestnum[3:-4]
            return num
        except:
            try:
                # time.sleep(5)
                self.wait_is_visible('x', '/html/body/div[1]/div[1]/ul/li[3]/h2/a')
                time.sleep(3)
                strguestnum = self.find_element_text('x', '/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/span')
                # 判断嘉宾的统计数字是否显示
                s = len(strguestnum[3:-4])
                if s == 0:
                    time.sleep(2)
                    strguestnum = self.find_element_text('x', '/html/body/div[1]/div[2]/div/div[1]/div[1]/div[1]/span')
                num = strguestnum[3:-4]
                return num
            except:
                self.deprint("获取嘉宾数量失败")




if __name__ == '__main__':
    dr = brower()
    o = LoginPage(dr)
    o.login()
    o = ChoosePage(dr)
    time.sleep(3)
    o.click_menu_bt('8')
    o =  Webinar_IndexPage(dr)
    time.sleep(3)
    o.index_webinar()
    guestnum = Get_Guestnum(dr)
    guestnum.get_num()