import asyncio

# 方案一
loop = asyncio.get_event_loop()

# 方案二
try:
    loop = asyncio.get_running_loop()
except RuntimeError:
    print("没有事件循环在运行")
