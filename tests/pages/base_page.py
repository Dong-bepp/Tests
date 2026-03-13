from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10) # 设置10秒显式等待

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        """封装查找元素方法，自带等待"""
        return self.wait.until(EC.presence_of_element_located(locator))

    def click(self, locator):
        """封装点击方法"""
        self.find_element(locator).click()

    def send_keys(self, locator, text):
        """封装输入方法"""
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)