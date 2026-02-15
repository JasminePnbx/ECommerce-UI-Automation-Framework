import pytest
from selenium.webdriver.common.by import By

@pytest.mark.regression
class TestCart:

    def test_add_to_cart(self, inventory_page):
        """添加商品到购物车"""
        inventory_page.add_items_to_cart()
        inventory_page.go_to_cart()
        assert "cart" in inventory_page.driver.current_url

    def test_cart_badge(self, inventory_page):
        """购物车角标数字正确"""
        inventory_page.add_items_to_cart()
        cart_badge = inventory_page.find_element((By.CLASS_NAME, "shopping_cart_badge"))
        assert cart_badge.text == "2"