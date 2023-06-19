import asyncio

async def main():
    print("Hello World")

loop = asyncio.get_event_loop()

loop.create_task(main())
try:
    loop.run_forever()
finally:
    loop.close()
"""
Hello World
"""

"""

任务可以先添加到事件循环中，然后调用 loop.run_forever() 启动事件循环，这样之前添加的任务
会自动执行。并且这个 run_forever() 将处于阻塞状态，直到我们显式调用 loop.stop() 或出现
异常时才会停止。

除了 loop.stop() 之外还有 loop.close()，loop.stop() 之后仍然可以调用 loop.run_* 方法，
但 loop.close() 不行，它会直接关闭事件循环。

"""