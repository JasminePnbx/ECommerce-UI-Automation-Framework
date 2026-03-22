import pytest
from config.settings import PRODUCT_BACKPACK, PRODUCT_BIKE_LIGHT
from pages.cart_page import CartPage


@pytest.mark.regression
class TestCart:

    def test_cart_contains_added_products(self, cart_page: CartPage) -> None:
        """
        购物车里应该包含之前加入的两个商品。
        通过商品名称验证，不是通过数量。
        """
        names = cart_page.get_cart_item_names()
        assert PRODUCT_BACKPACK   in names, f"购物车应含 {PRODUCT_BACKPACK}"
        assert PRODUCT_BIKE_LIGHT in names, f"购物车应含 {PRODUCT_BIKE_LIGHT}"

    def test_cart_item_count_is_correct(self, cart_page: CartPage) -> None:
        """购物车商品数量应为 2。"""
        assert cart_page.get_cart_item_count() == 2

    def test_checkout_success_message(self, cart_page: CartPage) -> None:
        """完成结账后显示成功信息。"""
        cart_page.checkout("QA", "Bot", "12345")
        assert "Thank you" in cart_page.get_success_message()