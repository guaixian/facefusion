#!/usr/bin/env python3
import threading
import subprocess
from facefusion import core
def run_script():
    print("启动后台脚本...")
    # 使用 subprocess 调用另一个 Python 脚本
    subprocess.run(["python", "exfec.py"])
    print("脚本执行完成")

# 创建一个线程，执行 run_script 函数

if __name__ == '__main__':
    # 启动 facefusion 的核心逻辑
    thread = threading.Thread(target=run_script)
    # 启动线程
    thread.start()
    core.cli()
