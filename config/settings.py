BASE_URL = "https://www.saucedemo.com"
TIMEOUT  = 10

USERS = [
    {"username": "standard_user",   "password": "secret_sauce", "should_succeed": True},
    {"username": "locked_out_user", "password": "secret_sauce", "should_succeed": False},
    {"username": "problem_user",    "password": "secret_sauce", "should_succeed": True},
]

# 测试用的商品名称，直接用页面显示的文字
PRODUCT_BACKPACK   = "Sauce Labs Backpack"
PRODUCT_BIKE_LIGHT = "Sauce Labs Bike Light"