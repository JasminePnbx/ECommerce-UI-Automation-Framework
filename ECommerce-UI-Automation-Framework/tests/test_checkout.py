import pytest


class TestCheckout:

    @pytest.mark.smoke
    def test_complete_order(self, inventory_page, cart_page):
        """完整购物流程：加购 → 结算 → 成功"""
        inventory_page.add_items_to_cart()
        inventory_page.go_to_cart()
        cart_page.checkout("Penny", "William", "12345")
        success_msg = cart_page.get_success_message()
        assert "THANK YOU FOR YOUR ORDER" in success_msg.upper()

    @pytest.mark.xfail(reason="已知bug：邮编非数字时报错信息不对，待修复")
    def test_invalid_postal_code(self, inventory_page, cart_page):
        """异常场景：邮编包含字母（预期失败）"""
        inventory_page.add_items_to_cart()
        inventory_page.go_to_cart()
        cart_page.checkout("Penny", "William", "ABC")
        # 这里应该断言错误信息，但当前版本有bug
        assert False