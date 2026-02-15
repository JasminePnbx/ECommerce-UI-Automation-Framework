from selenium.webdriver.common.by import By
from .base_page import BasePage


class InventoryPage(BasePage):
    CART_LINK = (By.CLASS_NAME, "shopping_cart_link")
    ADD_BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    ADD_BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    ITEM_NAME = (By.ID, "item_4_title_link")

    def go_to_detail(self):
        """点击商品标题，进入详情页"""
        self.click(self.ITEM_NAME)

    def add_items_to_cart(self):
        self.click(self.ADD_BACKPACK)
        self.click(self.ADD_BIKE_LIGHT)

    def go_to_cart(self):
        self.click(self.CART_LINK)