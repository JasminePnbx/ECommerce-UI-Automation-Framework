# ECommerce UI Automation Framework

基于 **POM（Page Object Model）** 三层架构的 Web UI 自动化测试框架，
被测系统为开源电商平台 [SauceDemo](https://www.saucedemo.com)。

## 架构设计
```
pages/    第一层：Page Object 封装（Locator + 操作方法，零业务断言）
tests/    第二层：测试用例（只写业务断言，零 Locator）
config/   配置层：URL、账号、超时等集中管理
```

## 核心设计决策

- **动态 XPath 定位**：通过商品名称动态生成 Locator，不依赖硬编码 ID，
  新增商品无需修改 Page 类
- **数据驱动**：pytest parametrize 覆盖正常登录、密码错误、账号锁定三种场景
- **xfail 标记**：对已知 bug 用 `@pytest.mark.xfail` 标记，
  区分"预期失败"和"真实失败"
- **CI 环境适配**：通过 `CI` 环境变量自动切换 headless 模式，
  本地有头运行，CI 无头运行

## 测试覆盖

| 模块 | 用例数 | 场景 |
|------|--------|------|
| 登录 | 5 | 正向、锁定账号、空字段、错误密码 |
| 商品列表 | 4 | 列表非空、加购角标、跳转购物车 |
| 商品详情 | 4 | 商品名、返回、加购、移除 |
| 购物车 | 3 | 商品验证、数量、结算成功 |
| 结算 | 2 | 完整流程、异常邮编（xfail）|

## 快速开始
```bash
pip install -r requirements.txt
pytest
```

## GitHub Actions CI

每次 push 自动触发测试，Allure 报告发布到 GitHub Pages。