import pytest

from pages.page_credit import CreditPage
from pages.page_login import LoginPage
from tools import DriverTools


@pytest.fixture(scope="function")
def login_page():
    # 创建浏览器对象
    driver = DriverTools.get_driver()
    # 创建登录页面对象
    page = LoginPage(driver)
    # 访问登录页面
    page.open_url("http://121.43.169.97:8081/common/member/login")
    yield page
    # 退出浏览器
    DriverTools.quit_driver()


@pytest.fixture(scope="function")
def credit_page(login_page):
    driver = DriverTools.get_driver()
    # 前置：输入url，登录
    # # 创建登录页面对象
    # login_page = LoginPage(driver)
    # login_page.open_url("http://121.43.169.97:8081/common/member/login")
    login_page.login("13800002011", "Aa123456")
    # 创建额度页面对象
    page = CreditPage(driver)
    yield page
    # 退出浏览器
    DriverTools.quit_driver()
