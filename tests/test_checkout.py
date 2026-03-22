import pytest
from config.settings import PRODUCT_BACKPACK, PRODUCT_BIKE_LIGHT


class TestCheckout:

    @pytest.mark.smoke
    def test_complete_order(self, cart_page):
        """
        完整购物流程：加购 → 结算 → 成功。
        cart_page fixture 已完成登录、加商品、进入购物车，
        这里直接结算即可。
        """
        cart_page.checkout("Penny", "William", "12345")
        success_msg = cart_page.get_success_message()
        assert "Thank you" in success_msg

    @pytest.mark.xfail(reason="已知bug：邮编非数字时报错信息不对，待修复")
    def test_invalid_postal_code(self, inventory_page, cart_page):
        """异常场景：邮编包含字母（预期失败）"""
        inventory_page.add_product_to_cart(PRODUCT_BACKPACK)
        inventory_page.go_to_cart()
        cart_page.checkout("Penny", "William", "ABC")
        assert False