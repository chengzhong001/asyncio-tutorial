import asyncio

async def main():
    print("Hello World")

# 获取事件循环直接通过 get_event_loop 即可
# 在没有的时候会自动创建
loop = asyncio.get_event_loop()
# 注：asyncio.create_task 只能在协程里面用
# 而 loop.create_task 在任何地方都可以
# 当然它们返回的都是 Task 对象
loop.create_task(main())
# 注意：此时事件循环虽然创建了，但是还没有运行
# 我们随便驱动一个协程，这样事件循环就运行起来了
# 然后会检测事件循环里面的任务，并驱动它们执行
loop.run_until_complete(asyncio.sleep(1))
"""
Hello World
"""

"""
回调函数和协程每次只能在预先设计好、并正在运行的事件循环上被调度。我们需要知道究竟该调用哪个循环 
API，以便将事件循环状态机（state machine）转换为运行状态。我们还需要确定正确的位置来调度
回调函数和协程。
"""