import asyncio


async def delay(seconds):
    print(f"开始休眠 {seconds} 秒")
    await asyncio.sleep(seconds)
    print("休眠完成")
    return seconds


async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(delay_task, 1)
        print("返回值:", result)
    except asyncio.TimeoutError:
        print("超时啦")
        # delay_task.cancelled() 用于判断任务是否被取消
        # 任务被取消：返回 True，没有被取消：返回 False
        print("任务是否被取消:", delay_task.cancelled())


asyncio.run(main())
"""
开始休眠 2 秒
超时啦
任务是否被取消: True
"""

"""
每秒（或其他时间间隔）执行检查然后取消任务，并不是处理超时的最简单方法。理想情况下，我们应该有一个辅助函数，它允许指定超时并自动取消任务。

asyncio 通过名为 asyncio.wait_for 的函数提供此功能，该函数接收协程或任务对象，以及以秒
为单位的超时时间。如果任务完成所需的时间超过了设定的超时时间，则会引发 
TimeoutException，任务将自动取消。

为说明 wait_for 的工作原理，我们使用一个案例来说明：有一个任务需要 2 秒才能完成，但我们
将它的超时时间设定为 1 秒。当得到一个 TimeoutError 异常时，我们将捕获异常，并检查任务
是否被取消。

注：使用 wait_for 必须要搭配 await，阻塞等待任务完成并拿到返回值、或者达到超时时间引发
TimeoutError 之后，程序才能往下执行。
"""