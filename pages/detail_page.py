import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class DetailPage(BasePage):
    _BACK_BTN = (By.CSS_SELECTOR, "[data-test='back-to-products']")
    _PRODUCT_NAME = (By.CSS_SELECTOR, ".inventory_details_name")
    _CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")

    # 🌟 终极解法：详情页只有这一个操作按钮，直接用类名定位，无视它动态变化的属性！
    _ACTION_BTN = (By.CSS_SELECTOR, ".btn_inventory")

    def get_product_name(self) -> str:
        return self._get_text(self._PRODUCT_NAME)

    def add_to_cart(self) -> "DetailPage":
        logger.info("detail: add_to_cart")
        self._click(self._ACTION_BTN)
        # 等待按钮文字变成 Remove
        self._wait.until(EC.text_to_be_present_in_element(self._ACTION_BTN, "Remove"))
        return self

    def remove_from_cart(self) -> "DetailPage":
        logger.info("detail: remove_from_cart")
        self._click(self._ACTION_BTN)
        # 等待按钮文字变回 Add to cart
        self._wait.until(EC.text_to_be_present_in_element(self._ACTION_BTN, "Add to cart"))
        return self

    def back_to_products(self) -> None:
        logger.info("detail: back_to_products")
        self._click(self._BACK_BTN)

    def get_cart_count(self) -> str:
        try:
            return self._get_text(self._CART_BADGE)
        except Exception:
            return ""