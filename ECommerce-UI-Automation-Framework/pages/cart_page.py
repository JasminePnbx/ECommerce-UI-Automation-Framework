from selenium.webdriver.common.by import By
from .base_page import BasePage


class CartPage(BasePage):
    CHECKOUT_BTN = (By.ID, "checkout")
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BTN = (By.ID, "continue")
    FINISH_BTN = (By.ID, "finish")
    COMPLETE_HEADER = (By.CLASS_NAME, "complete-header")

    def checkout(self, first_name, last_name, postal_code):
        self.click(self.CHECKOUT_BTN)
        self.input_text(self.FIRST_NAME, first_name)
        self.input_text(self.LAST_NAME, last_name)
        self.input_text(self.POSTAL_CODE, postal_code)
        self.click(self.CONTINUE_BTN)
        self.click(self.FINISH_BTN)

    def get_success_message(self):
        return self.get_text(self.COMPLETE_HEADER)