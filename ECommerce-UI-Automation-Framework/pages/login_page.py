from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    # 页面元素定位器（使用元组，便于传参）
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def login(self, username, password):
        self.input_text(self.USERNAME, username)
        self.input_text(self.PASSWORD, password)
        self.click(self.LOGIN_BTN)

    def get_error_message(self):
        return self.get_text(self.ERROR_MSG)

    def is_login_success(self):
        return "inventory" in self.driver.current_url