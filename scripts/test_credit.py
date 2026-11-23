from pages.page_credit import CreditPage
from pages.page_login import LoginPage
from scripts import log
from tools import DriverTools


class TestCredit:
    """测试类"""

    def test_01_credit_success(self):
        """额度申请成功"""
        # 创建浏览器对象
        driver = DriverTools.get_driver()
        # 前置：输入url，登录
        login_page = LoginPage(driver)
        login_page.open_url("http://121.43.169.97:8081/common/member/login")
        login_page.login("13800002011", "Aa123456")

        # 创建页面对象
        credit_page = CreditPage(driver)
        # 调用方法
        credit_page.credit_application("1000", "测试", "8888")
        # 获取结果
        result = credit_page.get_success_result()
        log.info(f"额度申请结果：{result}")
        # 断言
        assert "提交申请成功" in result
        # 截图
        credit_page.get_shot("额度申请截图")

    def test_00_credit_success(self,credit_page):
        """额度申请成功"""
        # 调用方法
        credit_page.credit_application("1000", "测试", "8888")
        # 获取结果
        result = credit_page.get_success_result()
        log.info(f"额度申请结果：{result}")
        # 断言
        assert "提交申请成功" in result
        # 截图
        credit_page.get_shot("额度申请截图")