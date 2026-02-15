import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import BASE_URL, TIMEOUT
from pages.detail_page import DetailPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


# 1. 浏览器驱动 fixture（参数化）
@pytest.fixture(params=["chrome", "edge"])  # 可添加firefox
def driver(request):
    """根据参数启动不同浏览器"""
    browser = request.param
    if browser == "chrome":
        options = Options()
        options.add_argument("--headless")  # 无头模式（CI环境用）
        driver = webdriver.Chrome(options=options)
    elif browser == "edge":
        driver = webdriver.Edge()
    else:
        raise ValueError(f"不支持的浏览器: {browser}")

    driver.implicitly_wait(TIMEOUT)
    driver.maximize_window()
    yield driver
    driver.quit()


# 2. 已登录状态的 fixture（依赖driver）
@pytest.fixture
def logged_in_driver(driver):
    """执行登录并返回已登录的driver"""
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")
    assert login_page.is_login_success(), "登录失败"
    yield driver
    # 后置操作：清理购物车（如果有必要）


# 3. 页面对象 fixture（简化测试代码）
@pytest.fixture
def login_page(driver):
    return LoginPage(driver)


@pytest.fixture
def inventory_page(logged_in_driver):
    return InventoryPage(logged_in_driver)


@pytest.fixture
def cart_page(logged_in_driver):
    return CartPage(logged_in_driver)

#detail页面自己写的
@pytest.fixture
def detail_page(logged_in_driver):
    return DetailPage(logged_in_driver)

# 4. 自动应用的 fixture（打印测试名）
@pytest.fixture(autouse=True)
def test_header(request):
    print(f"\n========== 开始执行: {request.node.name} ==========")
    yield
    print(f"\n========== 结束执行: {request.node.name} ==========")