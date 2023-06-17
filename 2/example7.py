import asyncio

async def delay(seconds):
    print(f"开始休眠 {seconds} 秒")
    await asyncio.sleep(seconds)
    print("休眠完成")
    return seconds

async def main():
    delay_task = asyncio.create_task(delay(2))
    try:
        # 通过 asyncio.shield 将 delay_task 保护起来
        result = await asyncio.wait_for(asyncio.shield(delay_task), 1)
        print("返回值:", result)
    except asyncio.TimeoutError:
        print("超时啦")
        # 如果超时依旧会引发 TimeoutError，但和之前不同的是
        # 此时任务不会被取消了，因为 asyncio.shield 会将取消请求忽略掉
        print("任务是否被取消:", delay_task.cancelled())
        # 从出现超时的地方，继续执行，并等待它完成
        result = await delay_task
        print("返回值:", result)

asyncio.run(main())
"""
开始休眠 2 秒
超时啦
任务是否被取消: False
休眠完成
返回值: 2
"""

"""
如果任务花费的时间比预期的长，在引发 TimeoutError 之后自动取消任务通常是个好主意。否则，
可能有一个协程无限期地等待，占用永远不会释放的资源。但在某些情况下，我们可能希望保持协程
运行。例如，我们可能想通知用户：某任务花费的时间比预期的要长，但即便超过了规定的超时时间，
也不取消该任务。为此，可使用 asyncio.shield 函数包装任务，这个函数将防止传入的协程被取
消，会给它一个屏蔽，将取消请求将忽略掉。

"""