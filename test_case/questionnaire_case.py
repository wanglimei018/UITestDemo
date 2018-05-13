# -*- coding: utf-8 -*-

import unittest
from test_case.base_unit import BaseUnit
from pages.common_pages.base import BasePage
from pages.common_pages.login_page import LoginPage
from pages.common_pages.choose_page import ChoosePage
from pages.common_pages.driver import brower
from pages.questionnaire_page.questionnaire_list_page import QuestionnaireListPage
from pages.questionnaire_page.question_bank_page import QuestionBankManagement

class Questionnaire(unittest.TestCase):
    """ 问卷测试用例 """
    def setUp(self):
        self.driver = brower()
        object = LoginPage(self.driver)
        object.login()

        object = ChoosePage(self.driver)
        object.click_menu_bt('11')

    def tearDown(self):
        self.driver.quit()

    def test_001_create_question(self):
        """创建问卷"""
        object = QuestionnaireListPage(self.driver)
        object.open_questionBank()
        object = QuestionBankManagement(self.driver)
        actual_result=object.create_question()
        expect_result="What is your favorite sport?"
        self.assertEqual(actual_result,expect_result,u"试题没有创建成功")
        object.delete_question()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Questionnaire("test_001_create_question"))
    runner = unittest.TextTestRunner()
    runner.run(suit)