import os
import shutil

if __name__ == "__main__":
    # 清理旧报告
    if os.path.exists("report"):
        shutil.rmtree("report")
        print("已删除旧报告目录")

    # 执行测试
    exit_code = os.system(
        "pytest -n 4 --reruns 2 --reruns-delay 1 "
        "--html=report/report.html --self-contained-html"
    )

    print("\n测试执行完成，报告已生成：report/report.html")
    exit(exit_code)