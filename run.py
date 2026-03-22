import os
import shutil

if __name__ == "__main__":
    # 1. 清理旧的 Allure 结果数据
    if os.path.exists("allure-results"):
        shutil.rmtree("allure-results")
        print("已清理旧的 allure-results 目录")

    # 2. 执行测试并生成 Allure 原生数据 (--alluredir=allure-results)
    print("\n========== 开始执行测试 ==========")
    exit_code = os.system(
        "pytest -n 4 --reruns 2 --reruns-delay 1 --alluredir=allure-results"
    )

    # 3. 自动生成并打开华丽的 Allure 报告
    print("\n========== 测试完成，正在启动 Allure 报告服务 ==========")
    os.system("allure serve allure-results")