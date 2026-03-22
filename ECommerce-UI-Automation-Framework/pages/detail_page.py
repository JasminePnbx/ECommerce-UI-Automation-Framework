from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DetailPage(BasePage):
    # 修正 ID
    BACK_BTN = (By.ID, 'back-to-products')
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-sauce-labs-backpack') # 假设点第一个包
    REMOVE_BTN = (By.ID, 'remove-sauce-labs-backpack')
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    def back_to_products(self):
        self.click(self.BACK_BTN)

    def click_add_to_cart(self):
        self.click(self.ADD_TO_CART_BTN)

    def click_remove(self):
        self.click(self.REMOVE_BTN)

    def get_cart_count(self):
        """获取购物车数量"""
        return self.get_text(self.CART_BADGE)

    # TWITTER=(By.CSS_SELECTOR,'a[data-test="social-twitter"]')
    # FACEBOOK=(By.CSS_SELECTOR,'a[data-test="social-facebook"]')
    # LINKEDIN = (By.CSS_SELECTOR, 'a[data-test="social-linkedin"]')
    # CART_BADGE=(By.CSS_SELECTOR,'span[data-test="shopping-card-badge"]')
    #
    # def back_to_product(self):
    #     self.click(self.BTN_SECOND)
    #
    # def add_to_cart(self):
    #     self.click(self.ADD_TO_CART)
    #
    # def remove(self):
    #     self.click(self.REMOVE_TO_CART)
    #
    # def get_cart_count(self):
    #     text = self.get_text(self.CART_BADGE)
    #     return int(text)  # 把字符串 "1" 变成数字 1，方便比较