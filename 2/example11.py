import time
import asyncio
from functools import wraps
from typing import Callable, Any


def async_timed(func: Callable) -> Callable:
    @wraps(func)
    async def wrapper(*args, **kwargs) -> Any:
        print(f"协程 {func.__name__} 开始执行")
        start = time.perf_counter()
        try:
            return await func(*args, **kwargs)
        finally:
            end = time.perf_counter()
            total = end - start
            print(f"协程 {func.__name__} 用 {total} 秒执行完毕")

    return wrapper


@async_timed
async def delay(seconds):
    print(f"协程开始休眠 {seconds} 秒")
    await asyncio.sleep(seconds)
    print(f"{seconds} 秒后，协程结束休眠")
    return seconds


@async_timed
async def main():
    task_one = asyncio.create_task(delay(2))
    task_two = asyncio.create_task(delay(3))

    await task_one
    await task_two


asyncio.run(main())
