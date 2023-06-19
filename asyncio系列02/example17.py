import asyncio
# from asyncio import get_event_loop_policy
import platform

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)

if platform.system() != "Windows":
    watcher = asyncio.get_child_watcher()
    watcher.attach_loop(loop)


"""
对于新创建的事件循环，还要附加到事件循环策略监视器中，以确保我们的事件循环可以监视
在 UNIX 系统上新生成的子进程的终止状态。
"""