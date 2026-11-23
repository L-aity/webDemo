# 按照PO设计模式，对页面对象进行封装
# 类：
# 类名：注册页面 --> PageRegister
# 属性：元素定位
# 方法：页面操作

# 对象：创建对象、调用方法
import time
from selenium.webdriver.common.by import By
from base.page_base import BasePage
from tools import DriverTools


class PageRegister(BasePage):
    """注册页面"""

    # 类属性（公共：当页面实现完成之后，页面元素就是固定的）
    phone = (By.ID, "phone")  # 手机号
    pwd = (By.ID, "password")  # 密码
    code = (By.ID, "verifycode")  # 验证码
    get_code = (By.ID, "get_phone_code")  # 获取验证码
    phone_code = (By.ID, "phone_code")  # 手机验证码
    reg_btn = (By.CLASS_NAME, "lg-btn")  # 注册按钮
    # 获取结果元素定位
    res1_loc = (By.TAG_NAME, "h1")
    # res2_loc = (By.CLASS_NAME, "reg-title") # 注册抢...
    res2_loc = (By.ID, "xubox_layer2")  # 弹框：提示xxx

    # def __init__(self, driver):
    #     """元素属性"""
    #     super().__init__(driver)
    #     self.phone = (By.ID, "phone")  # 手机号
    #     self.pwd = (By.ID, "password")  # 密码
    #     self.code = (By.ID, "verifycode")  # 验证码
    #     self.get_code = (By.ID, "get_phone_code")  # 获取验证码
    #     self.phone_code = (By.ID, "phone_code")  # 手机验证码
    #     self.reg_btn = (By.CLASS_NAME, "lg-btn")  # 注册按钮

    def input_phone(self, phone):
        """输入用户名"""
        # 原始：
        # 1.定位元素
        # 2.元素.send_keys(内容)
        # 当前：封装后，一行代码实现元素定位和输入
        self.base_input(self.phone, phone)

    def input_pwd(self, pwd):
        """输入密码"""
        self.base_input(self.pwd, pwd)

    def input_code(self, code):
        """输入验证码"""
        self.base_input(self.code, code)

    def click_get_code(self):
        """点击获取验证码"""
        self.base_click(self.get_code)
        time.sleep(2)

    def input_phone_code(self, phone_code):
        """输入手机验证码"""
        self.base_input(self.phone_code, phone_code)

    def click_reg_btn(self):
        """点击注册按钮"""
        self.base_click(self.reg_btn)

    def register(self, phone, pwd, code, phone_code):
        """注册流程"""
        self.input_phone(phone)
        self.input_pwd(pwd)
        self.input_code(code)
        self.click_get_code()
        self.input_phone_code(phone_code)
        self.click_reg_btn()

    def get_success_result(self):
        """获取结果"""
        return self.fd_element(self.res1_loc).text

    def get_fail_result(self):
        """获取失败结果"""
        return self.fd_special_element(self.res2_loc).text


# if __name__ == '__main__':
#     # 获取浏览器
#     driver = DriverTools.get_driver()
#     # 创建注册页面对象
#     reg = PageRegister(driver)
#     # 访问注册页面
#     reg.open_url("http://121.43.169.97:8081/common/member/reg")
#     #  注册
#     reg.register("13802350002", "Aa123456", "8888", "666666")
#     # 退出浏览器
#     DriverTools.quit_driver()
