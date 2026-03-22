# Web UI Automation Framework based on Selenium & Pytest

## 项目简介
基于 Python + Selenium + Pytest + POM 设计模式构建的企业级 Web UI 自动化测试框架。
针对 SauceDemo 电商系统实现了核心业务流程的自动化覆盖。

## 核心特性 (Key Features)
* **设计模式**：采用 Page Object Model (POM) 分层设计，实现页面逻辑与测试数据的分离。
* **测试框架**：使用 Pytest 管理用例，支持 Fixture 依赖注入与前后置处理。
* **数据驱动**：支持 JSON/YAML 数据驱动测试，实现单脚本覆盖多场景（如登录成功/失败）。
* **稳定性**：封装显式等待 (WebDriverWait) 与 异常捕获机制，解决元素异步加载导致的 Flaky Tests 问题。
* **可视化报告**：集成 Allure 测试报告，提供详尽的测试结果与失败截图。