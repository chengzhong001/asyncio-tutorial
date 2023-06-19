import asyncio
from asyncio import get_event_loop_policy

# 创建事件循环
loop = asyncio.new_event_loop()
# 设置在策略的 _local 属性中
# 调用 asyncio.get_event_loop 时，会直接返回
# 因为循环存在，就不会再创建了
asyncio.set_event_loop(loop)

print(
    asyncio.get_event_loop() is loop is get_event_loop_policy()._local._loop
)  # True

"""
最佳实践：对于主线程，在外部我们会调用 get_event_loop，在协程内部我们会调用 
get_running_loop；如果是子线程，那么在外部则需要 
new_event_loop + set_event_loop 来实现。
"""