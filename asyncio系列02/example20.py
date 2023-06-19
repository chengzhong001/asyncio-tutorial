
import asyncio

async def main():
    await asyncio.sleep(3)
    print("Hello World")

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_until_complete(asyncio.sleep(1))


"""
此时不会有任何输出，因为当 asyncio.sleep(1) 这个协程结束后，事件循环就直接停止了。
"""