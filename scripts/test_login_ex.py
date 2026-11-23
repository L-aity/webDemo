import pytest

from scripts import log
from tools import read_json


class TestLogin:
    """测试类"""
    # 定义形参名称
    arg_names = "phone, pwd,expect_result"
    # 获取参数化的数据
    arg_values = read_json("login_data.json")

    @pytest.mark.parametrize(arg_names, arg_values)
    def test_00_login(self, login_page, phone, pwd, expect_result):
        """登录用例"""
        try:
            # 调用登录方法
            login_page.login(phone, pwd)
            # 判断
            if expect_result == "登录成功":
                # 打印结果
                result = login_page.get_success_result()
            else:
                result = login_page.get_fail_result()
            # print(result)
            log.info(f"执行结果：{result}")
            # 断言
            assert expect_result in result
            # 截图
            login_page.get_shot("登录结果截图")
        except Exception as e:
            # print(f"执行异常：{e}")
            log.info(f"执行异常：{e}")
