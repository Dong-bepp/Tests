import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function") # 每个测试函数都会创建一个新的driver
def browser():
    # 自动下载和管理ChromeDriver
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver # 将driver传递给测试用例
    driver.quit() # 测试结束后关闭浏览器