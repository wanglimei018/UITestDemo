# -*- coding: utf-8 -*-
"""
os模块就是对操作系统进行操作，比如取文件的路径。

sys模块提供了一系列有关Python运行环境的变量和函数,例如：
#生成报告是报错，编码错误。python2.7默认使用ascii，设置成utf-8，python2.7以后不用setdefaultencoding了
   reload(sys)
  sys.setdefaultencoding('utf8')
"""
import sys
reload(sys)  #在解释器里修改的编码只能保证当次有效，在重启解释器后，会发现，编码又被重置为默认的ascii了
sys.setdefaultencoding('utf8')
import os
curPath = os.path.abspath(os.path.dirname(__file__)) #os.path.basename(path):返回所给路径path的最底层路径名或者是文件名；
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
from pages.off_line_meeting_pages.interaction_link_page import InteractionAndCancle
import time
import unittest
from pages.common_pages.base import BasePage
from test_case.base_unit import BaseUnit
from common.report import report
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.off_line_meeting_pages.index_page import IndexPage
from common.mail import email_oper
from pages.off_line_meeting_pages.new_meeting_page import NewMeetingPage

base = BasePage(object)



class Offline_Meeting_Test(BaseUnit):

    """线下会测试用例（创建线下会、添加互动环节、删除线下会）"""


    def test_001_loginoffline(self):
        #下面一句的文字，是通过Python的一种注释doc string，用于函数、类和方法的描述，HTMLTestRunner可以读取此类型注释
        """ 测试创建线下会 """

        base.deprint("开始执行登录，并进入线下会用例")
        dr = self.driver
        object = LoginPage(dr)
        object.login()
        object = ChoosePage(dr)
        object.click_menu_bt('10')
        object = IndexPage(dr)
        object.click_createunderline()
        object = NewMeetingPage(dr)
        actual_result = object.create_neww_offline()
        expected_result = u'线下会创建成功'
        self.assertEqual(actual_result, expected_result, msg="failed")
        base.deprint("创建线下会页面用例执行完成")



    def test_002_interaction(self):
         """ 添加互动环节"""

         base.deprint("开始执行登录，并进入添加线下会互动环节用例")
         dr = self.driver
         o = LoginPage(dr)
         o.login()
         o = ChoosePage(dr)
         o.click_menu_bt('10')
         o = IndexPage(dr)
         o.click_linelist('2')
         o = InteractionAndCancle(dr)
         acture_result=o.interaction_and_cancle('1')
         excepet_result="已添加互动环节"
         # self.assertEqual(acture_result,excepet_result,"failed")
         base.deprint( "添加线下会互动环节添加用例完成")

    def test_003_createoffline(self):
         """ 测试删除线下会 """

         base.deprint("开始执行登录，并进入删除线下会用例")
         dr = self.driver
         o = LoginPage(dr)
         o.login()
         o = ChoosePage(dr)
         o.click_menu_bt('10')
         o = IndexPage(dr)
         o.click_linelist('2')
         object = InteractionAndCancle(dr)
         actual_result = object.interaction_and_cancle('2')
         expected_result = u'取消会议成功'
         self.assertEqual(actual_result, expected_result, msg="failed")
         base.deprint("删除线下会用例完成")



if __name__ == "__main__":
    #全部用例按照数字顺序测试
    #unittest.main()
    StartTime = time.time()
    suite = unittest.TestSuite()
    # 指定单个单元测试（ 需要配置运行方式才能走main函数，参考https://www.cnblogs.com/youreyebows/p/7867508.html）
    suite.addTest(Offline_Meeting_Test("test_003_createoffline"))
    # suite.addTest(Offline_Meeting_Test("test_002_interaction"))
    # suite.addTest(Offline_Meeting_Test("test_003_createoffline"))


    #执行单元测试，生成报告
    AddSuite = report.AllReport()
    AddSuite.onlyneed_suite(suite)

    #发送邮件
    EndTime = time.time()
    PerformTime = EndTime - StartTime
    content ="test_createoffline"

    # SendEmail = email.SendEmailModel()
    SendEmail = email_oper.SendEmailModel()
    SendEmail.postreport_only(PerformTime,content)