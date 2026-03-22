# 测试环境URL
BASE_URL = "https://www.saucedemo.com"

# 测试账号（参数化用）
USERS = [
    {"username": "standard_user", "password": "secret_sauce", "should_succeed": True},
    {"username": "locked_out_user", "password": "secret_sauce", "should_succeed": False},
    {"username": "problem_user", "password": "secret_sauce", "should_succeed": True},
]

# 超时时间
TIMEOUT = 10