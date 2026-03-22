import pytest
from config.settings import PRODUCT_BACKPACK
from pages.detail_page import DetailPage
from pages.inventory_page import InventoryPage


class TestDetail:

    def test_detail_shows_correct_product_name(
        self, detail_page: DetailPage
    ) -> None:
        """详情页显示的商品名称应和点击的商品一致。"""
        assert detail_page.get_product_name() == PRODUCT_BACKPACK

    def test_back_to_products_navigates_correctly(
        self, detail_page: DetailPage
    ) -> None:
        """点击返回按钮，URL 跳回 inventory 页。"""
        detail_page.back_to_products()
        assert "inventory" in detail_page.get_current_url()

    def test_add_to_cart_from_detail_updates_badge(
        self, detail_page: DetailPage
    ) -> None:
        """从详情页加入购物车，角标变为 1。"""
        detail_page.add_to_cart()
        assert detail_page.get_cart_count() == "1"

    def test_remove_from_cart_on_detail_clears_badge(
        self, detail_page: DetailPage
    ) -> None:
        """加入后再移除，角标消失（返回空字符串）。"""
        detail_page.add_to_cart()
        detail_page.remove_from_cart()
        assert detail_page.get_cart_count() == ""