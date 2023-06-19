import asyncio

async def main1():
    await asyncio.sleep(1)
    print("我是 main1")

async def main2():
    await asyncio.sleep(2)
    print("我是 main2")

async def main3():
    await asyncio.sleep(3)
    print("我是 main3")

loop = asyncio.get_event_loop()
# 启动三个任务，并丢到事件循环中
# 但事件循环还没有启动，所以任务也不会执行
loop.create_task(main1(), name="main1")  # 创建任务时可以给任务起个名字
loop.create_task(main2(), name="main2")
loop.create_task(main3(), name="main3")

# 当调用 loop.for_ever 时，会启动事件循环，无限运行
# 直到我们调用 loop.stop 或 loop.close 时停止
# 当然也可以通过 loop.run_until_complete 运行一个协程，来启动事件循环
# 但这种方式启动的事件循环，会在 run_until_complete 里面的任务(协程)执行完毕后自动停止
loop.run_until_complete(asyncio.sleep(1.5))
"""
我是 main1
"""

# 所以此时 main1() 一定运行完了，但 main2() 和 main3() 显然没有
# 通过 asyncio.all_tasks(loop) 可以查看当前尚未运行完毕的所有任务
unfinished_tasks = asyncio.all_tasks(loop)
print(unfinished_tasks)
"""
{<Task pending name='main2' coro=<main2() running at .../main.py:8> wait_for=<Future pending..., 
 <Task pending name='main3' coro=<main3() running at .../main.py:12> wait_for=<Future pending...}
"""  # noqa: E501
# 返回一个集合，显然里面就是 main2 和 main3 两个没有完成的任务
t1 = unfinished_tasks.pop()
t2 = unfinished_tasks.pop()
print(t1.get_name(), t2.get_name())  
"""
main2 main3
"""

# 继续让它完成
loop.run_until_complete(t1)
"""
我是 main2
"""

async def contiune_run():
    await t2

loop.run_until_complete(contiune_run())
"""
我是 main3
"""


"""
任务要被添加到事件循环里面，但如果任务还没有运行完，事件循环就结束了该怎么办？就像上面那样，如何才能查看那些没有运行完的任务呢？
"""