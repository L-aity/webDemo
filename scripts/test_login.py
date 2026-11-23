
class TestLogin:
    """测试类"""

    def test_01_login_success(self, login_page):
        """登录成功"""
        # # 创建浏览器对象
        # driver = DriverTools.get_driver()
        # # 创建登录页面对象
        # login_page = LoginPage(driver)
        # # 访问登录页面
        # login_page.open_url("http://121.43.169.97:8081/common/member/login")
        # 调用登录方法
        login_page.login("13800002011", "Aa123456")
        # 打印结果
        result = login_page.get_success_result()
        print(result)
        # 断言
        assert "登录成功" in result
        # 退出浏览器
        # DriverTools.quit_driver()

    def test_02_login_pwd_error(self, login_page):
        """密码错误"""
        # # 创建浏览器对象
        # driver = DriverTools.get_driver()
        # # 创建登录页面对象
        # login_page = LoginPage(driver)
        # # 访问登录页面
        # login_page.open_url("http://121.43.169.97:8081/common/member/login")
        # 调用登录方法
        login_page.login("13800002011", "123456")
        # 获取结果
        result = login_page.get_fail_result()
        print(result)
        # 断言
        assert "密码错误" in result
        # 退出浏览器
        # DriverTools.quit_driver()

    def test_03_login_phone_not_exist(self, login_page):
        """手机号不存在"""
        # 调用登录方法
        login_page.login("13800008010", "Aa123456")
        result = login_page.get_fail_result()
        print(result)
        assert "用户不存在" in result
