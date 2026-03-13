# tests/test_cases/test_login_flow.py

import pytest
from pages.home_page import HomePage
from utils.data_provider import VALID_USER, INVALID_USER, EMPTY_CREDENTIALS

class TestLoginAndSearch:
    def test_successful_login(self, browser):
        """测试正确的用户名和密码可以登录成功"""
        home_page = HomePage(browser)
        home_page.login(VALID_USER["username"], VALID_USER["password"])
        assert "成功" in home_page.get_login_message()

    def test_failed_login_wrong_password(self, browser):
        """测试错误的密码登录失败"""
        home_page = HomePage(browser)
        home_page.login(INVALID_USER["username"], INVALID_USER["password"])
        assert "失败" in home_page.get_login_message()

    def test_failed_login_empty_fields(self, browser):
        """测试不输入任何信息点击登录"""
        home_page = HomePage(browser)
        home_page.login(EMPTY_CREDENTIALS["username"], EMPTY_CREDENTIALS["password"])
        assert "失败" in home_page.get_login_message()

    def test_search_for_algorithm_book(self, browser):
        """测试搜索“算法”能找到对应书籍"""
        home_page = HomePage(browser)
        home_page.search_for_book("算法导论")
        results = home_page.get_results_text()
        assert "算法导论" in results

    def test_search_no_results(self, browser):
        """测试搜索不存在的书显示无结果"""
        home_page = HomePage(browser)
        home_page.search_for_book("量子力学")
        results = home_page.get_results_text()
        assert "未找到" in results