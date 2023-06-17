import asyncio


async def delay(seconds):
    print(f"开始休眠 {seconds} 秒")
    await asyncio.sleep(seconds)
    print("休眠完成")
    return seconds


async def hello_from_second():
    for i in range(10):
        await asyncio.sleep(1)
        print("你好，我每秒钟负责打印一次")


async def main():
    asyncio.create_task(delay(3))
    asyncio.create_task(delay(3))

    await hello_from_second()


asyncio.run(main())
"""
开始休眠 3 秒
开始休眠 3 秒
你好，我每秒钟负责打印一次
你好，我每秒钟负责打印一次
休眠完成
休眠完成
你好，我每秒钟负责打印一次
你好，我每秒钟负责打印一次
你好，我每秒钟负责打印一次
你好，我每秒钟负责打印一次
你好，我每秒钟负责打印一次
你好，我每秒钟负责打印一次
你好，我每秒钟负责打印一次
你好，我每秒钟负责打印一次
"""


"""
创建任务是通过 asyncio.create_task 函数来实现的，当调用这个函数时，需要给它传递一个协
程，然后返回一个任务对象。一旦有了一个任务对象，就可以把它放在一个 await 表达式中，它完
成后就会提取返回值。

如果我们直接 await delay(3)，那么在打印之前需要至少等待 3 秒，但通过将它包装成任务，会
立即扔到事件循环里面运行。此时主程序可以直接往下执行，至于协程到底什么时候执行完毕、有没
有执行完毕，则通过 Task 对象（任务）来查看。当然你也可以 await 一个 Task 对象，保证里面
的协程运行完毕后才能往下执行。
"""