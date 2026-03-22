import pytest
from config.settings import USERS, BASE_URL


@pytest.mark.smoke  # 冒烟标记
class TestLogin:

    @pytest.mark.parametrize("user", USERS, ids=lambda u: u["username"])
    def test_login_scenarios(self, driver, login_page, user):
        driver.get(BASE_URL)
        """数据驱动：测试多组账号"""
        login_page.login(user["username"], user["password"])

        if user["should_succeed"]:
            assert login_page.is_login_success(), f"{user['username']} 应登录成功但失败"
        else:
            error_msg = login_page.get_error_message()
            assert "locked" in error_msg.lower(), f"{user['username']} 应被锁定"

    @pytest.mark.regression
    def test_login_page_ui(self, driver,login_page):
        driver.get(BASE_URL)
        """回归测试：登录页面元素是否存在"""
        assert login_page.find_element(login_page.USERNAME)
        assert login_page.find_element(login_page.PASSWORD)
        assert login_page.find_element(login_page.LOGIN_BTN)