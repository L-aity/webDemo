from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.page_base import BasePage


class LoginPage(BasePage):
    """登录页（TPshop）"""

    # 类属性：元素定位
    username = (By.ID, "username")  # 用户名（手机号/邮箱）
    pwd = (By.ID, "password")  # 密码
    verify_code = (By.ID, "verify_code")  # 验证码输入框
    verify_code_img = (By.ID, "verify_code_img")  # 验证码图片
    login_btn = (By.CSS_SELECTOR, ".J-login-submit")  # 登录按钮
    # 获取结果元素定位
    res_fail_loc = (By.CLASS_NAME, "layui-layer-content")  # 弹框：错误提示

    # 方法：页面操作(单步、业务)
    def input_username(self, username):
        """输入用户名"""
        self.base_input(self.username, username)

    def input_pwd(self, pwd):
        """输入密码"""
        self.base_input(self.pwd, pwd)

    def input_verify_code(self, verify_code):
        """输入验证码"""
        self.base_input(self.verify_code, verify_code)

    def click_verify_code_img(self):
        """点击验证码图片，刷新验证码"""
        self.base_click(self.verify_code_img)

    def click_login_btn(self):
        """点击登录按钮"""
        self.base_click(self.login_btn)

    def login(self, username, pwd, verify_code="8888"):
        """登录（万能验证码：8888）"""
        self.input_username(username)
        self.input_pwd(pwd)
        self.input_verify_code(verify_code)
        self.click_login_btn()

    def get_success_result(self):
        """获取登录成功结果（登录成功会跳转，返回跳转后的地址）"""
        WebDriverWait(self.driver, self.default_timeout).until(
            lambda d: "login" not in d.current_url.lower())
        return self.driver.current_url

    def get_fail_result(self):
        """获取登录失败结果（弹框提示文本）"""
        return self.fd_element(self.res_fail_loc).text
