import logging
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class CartPage(BasePage):
    _CHECKOUT_BTN    = (By.CSS_SELECTOR, "[data-test='checkout']")
    _FIRST_NAME      = (By.CSS_SELECTOR, "[data-test='firstName']")
    _LAST_NAME       = (By.CSS_SELECTOR, "[data-test='lastName']")
    _POSTAL_CODE     = (By.CSS_SELECTOR, "[data-test='postalCode']")
    _CONTINUE_BTN    = (By.CSS_SELECTOR, "[data-test='continue']")
    _FINISH_BTN      = (By.CSS_SELECTOR, "[data-test='finish']")
    _COMPLETE_HEADER = (By.CSS_SELECTOR, ".complete-header")
    _CART_ITEMS      = (By.CSS_SELECTOR, ".cart_item")
    _ITEM_NAMES      = (By.CSS_SELECTOR, ".inventory_item_name")

    def get_cart_item_names(self) -> list[str]:
        """返回购物车里所有商品名称。"""
        elements = self._driver.find_elements(*self._ITEM_NAMES)
        return [e.text for e in elements]

    def get_cart_item_count(self) -> int:
        """返回购物车商品数量。"""
        return len(self._driver.find_elements(*self._CART_ITEMS))

    def checkout(self, first_name: str, last_name: str, postal_code: str) -> None:
        logger.info("checkout | %s %s", first_name, last_name)
        self._click(self._CHECKOUT_BTN)
        self._input(self._FIRST_NAME, first_name)
        self._input(self._LAST_NAME, last_name)
        self._input(self._POSTAL_CODE, postal_code)
        self._click(self._CONTINUE_BTN)
        self._click(self._FINISH_BTN)

    def get_success_message(self) -> str:
        return self._get_text(self._COMPLETE_HEADER)