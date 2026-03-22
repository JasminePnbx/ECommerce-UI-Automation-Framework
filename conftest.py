import pytest
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config.settings import BASE_URL, TIMEOUT
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.detail_page import DetailPage

logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s [%(levelname)-8s] %(name)s - %(message)s",
    datefmt="%H:%M:%S",
)


@pytest.fixture
def driver():
    """Chrome headless driver，CI 和本地都可用。"""
    opts = Options()
    opts.add_argument("--headless=new")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--window-size=1920,1080")
    _driver = webdriver.Chrome(options=opts)
    _driver.implicitly_wait(0)   # 禁用隐式等待，强制使用显式等待
    yield _driver
    _driver.quit()


@pytest.fixture
def login_page(driver):
    return LoginPage(driver).navigate()


@pytest.fixture
def inventory_page(driver):
    """已登录状态的商品列表页。"""
    LoginPage(driver).navigate().login("standard_user", "secret_sauce")
    return InventoryPage(driver)


@pytest.fixture
def cart_page(driver):
    """已登录并进入购物车页。"""
    LoginPage(driver).navigate().login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    from config.settings import PRODUCT_BACKPACK, PRODUCT_BIKE_LIGHT
    inventory.add_product_to_cart(PRODUCT_BACKPACK)
    inventory.add_product_to_cart(PRODUCT_BIKE_LIGHT)
    inventory.go_to_cart()
    return CartPage(driver)


@pytest.fixture
def detail_page(driver):
    """已登录并进入第一个商品详情页。"""
    from config.settings import PRODUCT_BACKPACK
    LoginPage(driver).navigate().login("standard_user", "secret_sauce")
    inventory = InventoryPage(driver)
    inventory.click_product(PRODUCT_BACKPACK)
    return DetailPage(driver)