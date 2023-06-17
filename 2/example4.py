import asyncio


async def delay(seconds):
    print(f"开始休眠 {seconds} 秒")
    await asyncio.sleep(seconds)
    print("休眠完成")
    return seconds


async def main():
    long_task = asyncio.create_task(delay(3))
    # 立刻取消
    long_task.cancel()
    # 但 CancelledError 只有在 await 取消的协程时才会触发
    # 所以下面的语句会正常执行
    print("我会正常执行")
    print("Hello World")
    print(list(range(10)))
    await asyncio.sleep(5)
    try:
        # 引发 CancelledError
        await long_task
    except asyncio.CancelledError:
        print("任务被取消")


asyncio.run(main())
"""
我会正常执行
Hello World
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
任务被取消
"""

"""
关于取消任务需要注意的是，CancelledError 只能从 await 语句抛出。这意味着如果在任务在执行
普通 Python 代码时被取消，那么该代码将一直运行，直到触发下一个 await 语句（如果存在），
才能引发 CancelledError。
"""
