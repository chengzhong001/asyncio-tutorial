import asyncio

async def set_future_value(future):
    await asyncio.sleep(1)
    future.set_result("Hello World")

def make_request():
    future = asyncio.Future()
    # 创建一个任务来异步设置 future 的值
    asyncio.create_task(set_future_value(future))
    return future

async def main():
    # 注意这里的 make_request，它是一个普通的函数，如果在外部直接调用肯定是会报错的
    # 因为没有事件循环，在执行 set_future_value 时会报错
    # 但如果在协程里面调用是没问题的，因为协程运行时，事件循环已经启动了
    # 此时在 make_request 里面，会启动一个任务
    future = make_request()
    print(f"future 是否完成: {future.done()}")
    # 阻塞等待，直到 future 有值，什么时候有值呢？
    # 显然是当协程 set_future_value 里面执行完 future.set_result 的时候
    value = await future  # 暂停 main()，直到 future 的值被设置完成
    print(f"future 是否完成: {future.done()}")
    print(value)

asyncio.run(main())
"""
future 是否完成: False
future 是否完成: True
Hello World
"""
