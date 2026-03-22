import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC  # 🌟 关键：引入 EC！
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class DetailPage(BasePage):
    _BACK_BTN      = (By.CSS_SELECTOR, "[data-test='back-to-products']")
    _ADD_TO_CART   = (By.CSS_SELECTOR, "[data-test='add-to-cart']")
    _REMOVE_BTN    = (By.CSS_SELECTOR, "[data-test='remove']")
    _PRODUCT_NAME  = (By.CSS_SELECTOR, ".inventory_details_name")
    _CART_BADGE    = (By.CSS_SELECTOR, ".shopping_cart_badge")

    def get_product_name(self) -> str:
        return self._get_text(self._PRODUCT_NAME)

    def add_to_cart(self) -> "DetailPage":
        logger.info("detail: add_to_cart")
        self._click(self._ADD_TO_CART)
        # 🌟 智能等待：点完“添加”，死死盯住直到“移除”按钮在页面上出现
        self._wait.until(EC.visibility_of_element_located(self._REMOVE_BTN))
        return self

    def remove_from_cart(self) -> "DetailPage":
        logger.info("detail: remove_from_cart")
        self._click(self._REMOVE_BTN)
        # 🌟 智能等待：点完“移除”，死死盯住直到“添加”按钮重新出现
        self._wait.until(EC.visibility_of_element_located(self._ADD_TO_CART))
        return self

    def back_to_products(self) -> None:
        logger.info("detail: back_to_products")
        self._click(self._BACK_BTN)

    def get_cart_count(self) -> str:
        try:
            return self._get_text(self._CART_BADGE)
        except Exception:
            return ""