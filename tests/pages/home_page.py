# tests/pages/home_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from .base_page import BasePage

class HomePage(BasePage):
    # 首页地址
    URL = "http://localhost:8080/index.html"

    # 登录相关元素
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//form[@id='loginForm']//button")  # 登录按钮
    LOGIN_MESSAGE_TEXT = (By.ID, "message")

    # 搜索相关元素
    SEARCH_BOX = (By.ID, "searchBox")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(text(), '搜索')]")
    RESULTS_LIST = (By.ID, "results")

    def __init__(self, driver):
        super().__init__(driver)
        self.open(self.URL)

    # --- 登录相关方法 ---
    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_SUBMIT_BUTTON)

    def get_login_message(self):
        return self.find_element(self.LOGIN_MESSAGE_TEXT).text

    # --- 搜索相关方法 ---
    def search_for_book(self, book_name):
        self.send_keys(self.SEARCH_BOX, book_name)
        self.click(self.SEARCH_BUTTON)

    def get_results_text(self):
        self.wait.until(EC.visibility_of_element_located(self.RESULTS_LIST))
        return self.find_element(self.RESULTS_LIST).text