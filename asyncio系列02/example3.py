import asyncio

async def delay(seconds):
    print(f"开始休眠 {seconds} 秒")
    await asyncio.sleep(seconds)
    print("休眠完成")
    return seconds

async def main():
    long_task = asyncio.create_task(delay(10))
    seconds_elapsed = 0

    while not long_task.done():
        print("检测到任务尚未完成，一秒钟之后继续检测")
        await asyncio.sleep(1)
        seconds_elapsed += 1
        # 时间超过 5 秒，取消任务
        if seconds_elapsed == 5:
            long_task.cancel()
    
    try:
        # 等待 long_task 完成，显然执行到这里的时候，任务已经被取消
        # 不管是 await 一个已经取消的任务，还是 await 的时候任务被取消
        # 都会引发 asyncio.CancelledError
        await long_task
    except asyncio.CancelledError:
        print("任务被取消")

asyncio.run(main())

"""
检测到任务尚未完成，一秒钟之后继续检测
开始休眠 10 秒
检测到任务尚未完成，一秒钟之后继续检测
检测到任务尚未完成，一秒钟之后继续检测
检测到任务尚未完成，一秒钟之后继续检测
检测到任务尚未完成，一秒钟之后继续检测
检测到任务尚未完成，一秒钟之后继续检测
任务被取消
"""

"""
取消任务很简单，每个任务对象都有一个名为 cancel 的方法，可以在想要停止任务时调用它。取消
一个任务将导致该任务在执行 await 时引发 CancelledError，然后再根据需要处理它。

为说明这一点，假设启动了一个长时间运行的任务，但我们不希望它运行的时间超过 5 秒。如果任
务没有在 5 秒内完成，就可以停止该任务，并向用户报告：该任务花费了太长时间，我们正在停止
它。我们还希望每秒钟都输出一个状态更新，为用户提供最新信息，这样就可以让用户了解任务的运行状态。

在代码中我们创建了一个任务，它需要花费 10 秒的时间才能运行完成。然后创建一个 while 循环
来检查该任务是否已完成，任务的 done 方法在任务完成时返回 True，否则返回 False。每一秒，
我们检查任务是否已经完成，并记录到目前为止经历了多少秒。如果任务已经花费了 5 秒，就取消
这个任务。然后来到 await long_task，将输出 "任务被取消"，这表明捕获了一个 CancelledError
"""