import asyncio
import threading

def create_loop():
    # 获取事件循环策略，如果没创建，那么就实例化 DefaultEventLoopPolicy 创建一个
    # 这个 DefaultEventLoopPolicy 也不是一个具体的类，而是根据操作系统会对应不同的类
    loop_policy = asyncio.get_event_loop_policy()
    # 通过策略的 new_event_loop 方法创建事件循环
    loop = loop_policy.new_event_loop()
    # 但以上两步可以直接合成一步，通过 asyncio.new_event_loop

    # 设置循环，将循环设置在策略的 _local 中，这样才能通过 get_event_loop 获取
    asyncio.set_event_loop(loop)
    loop.close()


threading.Thread(target=create_loop).start()
threading.Thread(target=create_loop).start()
threading.Thread(target=create_loop).start()

"""
以上我们就创建了 3 个事件循环，并保存在了策略的 _local 属性下面。

总结：事件循环策略在整个进程内是单例的，所有的线程共享一个策略；事件循环在所在的线程内是
单例的，一个线程内部只会有一个事件循环。所有线程对应的循环均位于策略的 _local 属性中，
获取的时候根据线程 ID 区分。

策略的 new_event_loop 方法：创建事件循环；
策略的 set_event_loop 方法：设置事件循环；
策略的 get_event_loop 方法：获取事件循环，会先检测策略的 _local 中是否有当前线程对应的
事件循环，有则获取，没有则通过 new_event_loop 创建、set_event_loop 设置，然后返回；

但是 get_event_loop、set_event_loop、new_event_loop 我们一般不会手动通过策略去调用，而是
会通过 asyncio 会去调用，比如 asyncio.get_event_loop。当然在 asyncio.get_event_loop 
内部，也是先通过 get_event_loop_policy() 获取策略，然后调用策略的 get_event_loop 方法，
获取线程对应的循环，两者本质是一样的，因为策略是单例的。

所以无论主线程还是子线程，毫无疑问都是可以创建事件循环的。只不过主线程既可以手动调用 
new_event_loop 和 set_event_loop 来创建，也可以调用 get_event_loop（当循环不存在时内部
自动创建）。但对于子线程而言，只能采用第一种方式，也就是手动创建，如果直接调用 
get_event_loop 是会报错的
"""
