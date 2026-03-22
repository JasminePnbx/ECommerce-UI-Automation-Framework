import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class LoginPage(BasePage):
    # Locator 集中管理，使用 data-test 属性最稳定
    _USERNAME  = (By.CSS_SELECTOR, "[data-test='username']")
    _PASSWORD  = (By.CSS_SELECTOR, "[data-test='password']")
    _LOGIN_BTN = (By.CSS_SELECTOR, "[data-test='login-button']")
    _ERROR_MSG = (By.CSS_SELECTOR, "[data-test='error']")

    def navigate(self) -> "LoginPage":
        self._driver.get("https://www.saucedemo.com")
        logger.info("navigate to login page")
        return self

    def login(self, username: str, password: str) -> "LoginPage":
        logger.info("login | user=%s", username)
        self._input(self._USERNAME, username)
        self._input(self._PASSWORD, password)
        self._click(self._LOGIN_BTN)
        return self

    def get_error_message(self) -> str:
        return self._get_text(self._ERROR_MSG)

    def is_login_successful(self) -> bool:
        return "inventory" in self.get_current_url()