# 使用pytest框架管理用例
from tools import DriverTools
from pages.page_register import PageRegister


class TestRegister:

    def setup_method(self):
        # 调用方法
        driver = DriverTools.get_driver()
        self.reg = PageRegister(driver)
        self.reg.open_url("http://121.43.169.97:8081/common/member/reg")

    def teardown_method(self):
        # 退出浏览器
        DriverTools.quit_driver()

    def test_01_register_success(self):
        """注册成功"""
        # 准备数据
        # 调用注册方法
        self.reg.register("13802390002", "Aa123456", "8888", "666666")
        # 打印结果
        result = self.reg.get_success_result()
        print(result)
        # 断言
        assert "注册成功" in result

    def test_02_register_phone_exist(self):
        """手机号已存在"""
        # # 获取浏览器
        # driver = DriverTools.get_driver()
        # # 创建注册页面对象
        # reg = PageRegister(driver)
        # # 访问注册页面
        # reg.open_url("http://121.43.169.97:8081/common/member/reg")
        #  注册
        self.reg.register("13802380002", "Aa123456", "8888", "666666")
        # 获取结果
        result = self.reg.get_fail_result()
        print(result)
        # 断言
        # assert "注册抢88现金" in result
        assert "手机已存在!" in result
        # 退出浏览器
        DriverTools.quit_driver()
