import asyncio

async def main():
    pass

asyncio.run(main())
loop = asyncio.get_event_loop()
"""
RuntimeError: There is no current event loop in thread 'MainThread'.
"""

"""
使用 asyncio.run 之后，就不能再调用 get_event_loop 了
"""