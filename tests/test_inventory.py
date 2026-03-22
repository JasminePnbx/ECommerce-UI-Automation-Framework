import pytest
from config.settings import PRODUCT_BACKPACK, PRODUCT_BIKE_LIGHT
from pages.inventory_page import InventoryPage


@pytest.mark.regression
class TestInventory:

    def test_product_list_not_empty(self, inventory_page: InventoryPage) -> None:
        """商品列表页应至少有一个商品。"""
        names = inventory_page.get_all_product_names()
        assert len(names) > 0

    def test_add_single_product_updates_badge(
        self, inventory_page: InventoryPage
    ) -> None:
        """
        通过商品名称加入购物车，角标数字变为 1。
        使用动态 XPath 定位，不依赖硬编码 ID。
        """
        inventory_page.add_product_to_cart(PRODUCT_BACKPACK)
        assert inventory_page.get_cart_count() == "1"

    def test_add_two_products_updates_badge(
        self, inventory_page: InventoryPage
    ) -> None:
        """加入两个商品，角标数字变为 2。"""
        inventory_page.add_product_to_cart(PRODUCT_BACKPACK)
        inventory_page.add_product_to_cart(PRODUCT_BIKE_LIGHT)
        assert inventory_page.get_cart_count() == "2"

    def test_go_to_cart_navigates_correctly(
        self, inventory_page: InventoryPage
    ) -> None:
        """点击购物车图标，URL 跳转到 cart 页面。"""
        inventory_page.go_to_cart()
        assert "cart" in inventory_page.get_current_url()