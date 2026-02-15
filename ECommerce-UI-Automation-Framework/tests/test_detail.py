
class TestDetail:
    def test_detail_back_to_product(self, inventory_page,detail_page):
        inventory_page.go_to_detail()
        detail_page.back_to_product()
        assert "inventory" in detail_page.driver.current_url

    def test_add_item_to_cart(self, detail_page):
        inventory_page.go_to_detail()
        detail_page.add_to_cart()
        current_count = detail_page.get_cart_count()
        assert current_count == 1

