from selenium.webdriver.common.by import By
from base.page_base import BasePage


class CreditPage(BasePage):
    # 类属性：元素定位
    role_loc = By.XPATH, '//*[@id="mlayout"]/div[2]/div[2]/div[1]/a/em'
    app_loc = By.XPATH, '//*[@id="mlayout"]/div[2]/div[2]/div[3]/div[2]/dl/dd[4]/a'
    amount_loc = By.ID, 'amount_account'
    detail_loc = By.NAME, 'remark'
    code_loc = By.ID, 'verifycode'
    submit_loc = By.CSS_SELECTOR, '.btn-submit.btn-md'
    # 获取结果元素定位
    res_success_loc = (By.ID, 'xubox_layer1')

    # 方法：页面操作(单步、业务)
    def click_role(self):
        """点击角色"""
        self.base_click(self.role_loc)

    def click_app(self):
        """点击额度申请"""
        self.base_click(self.app_loc)

    def input_amount(self, amount):
        """输入额度"""
        self.base_input(self.amount_loc, amount)

    def input_detail(self, detail):
        """输入用途"""
        self.base_input(self.detail_loc, detail)

    def input_code(self, code):
        """输入验证码"""
        self.base_input(self.code_loc, code)

    def click_submit(self):
        """点击提交"""
        self.base_click(self.submit_loc)

    def credit_application(self, amount, detail, code):
        """额度申请"""
        self.click_role()
        self.click_app()
        self.input_amount(amount)
        self.input_detail(detail)
        self.input_code(code)
        self.click_submit()

    def get_success_result(self):
        """获取成功结果"""
        return self.fd_element(self.res_success_loc).text