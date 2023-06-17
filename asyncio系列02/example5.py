import asyncio

async def delay(seconds):
    print(f"开始休眠 {seconds} 秒")
    await asyncio.sleep(seconds)
    print("休眠完成")
    return seconds

async def main():
    long_task = asyncio.create_task(delay(3))
    await asyncio.sleep(5)
    # 显然执行到这里，任务已经结束了
    long_task.cancel()
    try:
        await long_task
        print("任务执行完毕")
    except asyncio.CancelledError:
        print("任务被取消")

asyncio.run(main())
"""
开始休眠 3 秒
休眠完成
任务执行完毕
"""


"""
注意：如果任务在取消的时候已经运行完毕了，那么 await 的时候就不会抛 CancelledError 了。
"""