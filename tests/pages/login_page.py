from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    # 定义页面元素的定位器 (Locator)
    URL = "http://localhost:8080/login.html"
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SUBMIT_BUTTON = (By.TAG_NAME, "button") # 假设页面只有一个button
    MESSAGE_TEXT = (By.ID, "message")

    def __init__(self, driver):
        super().__init__(driver)
        self.open(self.URL)

    def login(self, username, password):
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.SUBMIT_BUTTON)

    def get_message(self):
        return self.find_element(self.MESSAGE_TEXT).text