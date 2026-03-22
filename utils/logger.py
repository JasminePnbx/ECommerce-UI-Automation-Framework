# utils/logger.py
import logging
import os
import time

class Logger:
    def __init__(self, logger_name="TestLogger"):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(logging.DEBUG)

        # 防止重复打印日志
        if not self.logger.handlers:
            # 1. 确定日志路径
            log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
            if not os.path.exists(log_path):
                os.mkdir(log_path)

            # 2. 日志文件名 (带时间戳)
            current_time = time.strftime('%Y%m%d_%H%M%S', time.localtime())
            log_file = os.path.join(log_path, f'{current_time}.log')

            # 3. 文件处理器 (写入文件)
            fh = logging.FileHandler(log_file, encoding='utf-8')
            fh.setLevel(logging.INFO)

            # 4. 控制台处理器 (输出到屏幕)
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 5. 格式器
            formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    def get_logger(self):
        return self.logger

# 单例模式：直接导出的实例
logger = Logger().get_logger()