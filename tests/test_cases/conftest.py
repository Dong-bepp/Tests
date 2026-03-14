import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options  # ✅ 新增导入
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="function")  # 每个测试函数都会创建一个新的 driver
def browser():
    # ✅ 创建 Chrome 选项对象，用于配置无头模式等参数
    chrome_options = Options()
    chrome_options.add_argument("--headless")              # 无界面模式（GitHub Actions 必需）
    chrome_options.add_argument("--no-sandbox")             # 禁用沙盒（Linux 环境必需）
    chrome_options.add_argument("--disable-dev-shm-usage")  # 避免 /dev/shm 空间不足

    # 自动下载和管理 ChromeDriver
    service = Service(ChromeDriverManager().install())

    # ✅ 启动 Chrome 时传入 options 参数
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # ❌ 注意：无头模式下无法最大化窗口，所以 driver.maximize_window() 要删除或注释掉
    # driver.maximize_window()  # 在 Headless 模式下无效，建议移除

    yield driver  # 将 driver 传递给测试用例

    driver.quit()  # 测试结束后关闭浏览器