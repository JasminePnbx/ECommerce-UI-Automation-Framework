import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

logger = logging.getLogger(__name__)


class InventoryPage(BasePage):
    _CART_LINK  = (By.CSS_SELECTOR, ".shopping_cart_link")
    _CART_BADGE = (By.CSS_SELECTOR, ".shopping_cart_badge")
    _ITEM_NAMES = (By.CSS_SELECTOR, ".inventory_item_name")

    def _add_to_cart_locator(self, product_name: str) -> tuple:
        return (
            By.XPATH,
            f"//div[text()='{product_name}']"
            f"/ancestor::div[contains(@class,'inventory_item')]"
            f"//button"
        )

    def add_product_to_cart(self, product_name: str) -> "InventoryPage":
        """通过商品名称加入购物车，不依赖硬编码 ID。"""
        logger.info("add_product_to_cart | product=%s", product_name)
        locator = self._add_to_cart_locator(product_name)

        # 1. 点击加入购物车
        self._click(locator)

        # 🌟【修复核心】：加购后，死死盯着这个按钮，直到它的文字变成 "Remove"，才允许代码往下走！
        self._wait.until(EC.text_to_be_present_in_element(locator, "Remove"))

        return self

    def go_to_cart(self) -> None:
        logger.info("go_to_cart")
        self._click(self._CART_LINK)

    def get_cart_count(self) -> str:
        """返回购物车角标数字，购物车为空时返回空字符串。"""
        try:
            return self._get_text(self._CART_BADGE)
        except Exception:
            return ""

    def click_product(self, product_name: str) -> None:
        """点击商品名称进入详情页。"""
        locator = (By.XPATH, f"//div[text()='{product_name}']")
        self._click(locator)
        logger.info("click_product | product=%s", product_name)

    def get_all_product_names(self) -> list[str]:
        """返回当前页面所有商品名称列表。"""
        elements = self._driver.find_elements(*self._ITEM_NAMES)
        return [e.text for e in elements]