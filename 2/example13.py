import asyncio

def some_func():
    print("我将稍后被调用")

async def main():
    # 协程需要扔到事件循环里面运行，而当协程运行的时候，也可以获取所在的事件循环
    loop = asyncio.get_running_loop()
    loop.call_soon(some_func)
    await asyncio.sleep(1)

loop = asyncio.new_event_loop()
try:
    loop.run_until_complete(main())
finally:
    loop.close()
"""
我将稍后被调用
"""
