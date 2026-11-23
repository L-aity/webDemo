from selenium.webdriver.common.by import By

from base.page_base import BasePage


class LoginPage(BasePage):
    """登录页"""

    # 类属性：元素定位
    phone = (By.ID, "keywords")
    pwd = (By.ID, "password")
    login_btn = (By.ID, "login-btn")
    # 获取成功元素定位
    res_success_loc = (By.ID, "xubox_layer1")
    res_fail_loc = (By.CSS_SELECTOR, '[ng-bind="loginErr"]')

    # 方法：页面操作(单步、业务)
    def input_phone(self, phone):
        """输入手机号"""
        self.base_input(self.phone, phone)

    def input_pwd(self, pwd):
        """输入密码"""
        self.base_input(self.pwd, pwd)

    def click_login_btn(self):
        """点击登录按钮"""
        self.base_click(self.login_btn)

    def login(self, phone, pwd):
        """登录"""
        self.input_phone(phone)
        self.input_pwd(pwd)
        self.click_login_btn()

    def get_success_result(self):
        """获取成功结果"""
        return self.fd_element(self.res_success_loc).text

    def get_fail_result(self):
        """获取失败结果"""
        return self.fd_element(self.res_fail_loc).text
