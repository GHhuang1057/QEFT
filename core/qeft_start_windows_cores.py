
import sys
import os
from res.edl.edlclient.Library.api import *



# 获取项目根目录
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 将项目根目录添加到 sys.path
sys.path.insert(0, project_root)

# 打印 sys.path 进行调试
print("sys.path:", sys.path)


# 步骤 1: 初始化和设置
e = edl_api()                # 实例化 API 对象
e.set_arg("--debugmode", True) # 启用调试模式
if (e.init() == 1):          # 初始化 API，检查状态
    exit(1)                  # 如果初始化失败 (status=1)，退出程序


# 步骤 1: 初始化和设置
e = edl_api()                # 实例化 API 对象
e.set_arg("--debugmode", True) # 启用调试模式
if (e.init() == 1):          # 初始化 API，检查状态
    exit(1)                  # 如果初始化失败 (status=1)，退出程序

# 步骤 2: 执行命令 (带调试模式)
e.peek(0x100000, 80, "peek1.bin") # 执行 peek 命令

# 步骤 3: 更改选项并重新初始化
e.reset_arg("--debugmode")      # 将 --debugmode 重置为默认值 (禁用)
if (e.reinit() == 1):         # 重新初始化 API 使更改生效，检查状态
    exit(1)                  # 如果重新初始化失败，退出程序

# 步骤 4: 执行命令 (不带调试模式)
e.peek(0x100080, 80, "peek2.bin") # 执行另一个 peek 命令

# 步骤 5: 设备操作
e.reset()                     # 使用 reset 命令重启安卓设备