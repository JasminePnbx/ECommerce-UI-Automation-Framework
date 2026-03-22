import pytest
from config.settings import USERS, BASE_URL
from pages.login_page import LoginPage


@pytest.mark.smoke
class TestLogin:

    @pytest.mark.parametrize("user", USERS, ids=lambda u: u["username"])
    def test_login_scenarios(self, login_page: LoginPage, user: dict) -> None:
        """数据驱动：正向登录成功 + 负向账号锁定。"""
        login_page.login(user["username"], user["password"])

        if user["should_succeed"]:
            assert login_page.is_login_successful(), \
                f"{user['username']} 应登录成功但失败"
        else:
            error_msg = login_page.get_error_message()
            assert "locked" in error_msg.lower(), \
                f"{user['username']} 应被锁定，实际错误: {error_msg!r}"

    def test_empty_credentials_show_error(self, login_page: LoginPage) -> None:
        """空用户名密码提交，应显示错误提示。"""
        login_page.login("", "")
        assert login_page.get_error_message() != ""

    def test_wrong_password_shows_error(self, login_page: LoginPage) -> None:
        """错误密码，应显示错误提示。"""
        login_page.login("standard_user", "wrong_password")
        assert "do not match" in login_page.get_error_message().lower()