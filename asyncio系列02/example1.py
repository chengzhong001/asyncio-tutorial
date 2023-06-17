import asyncio


async def delay(seconds):
    print(f"开始休眠 {seconds} 秒")
    await asyncio.sleep(seconds)
    print("休眠完成")
    return seconds


async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_once_more = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_once_more


asyncio.run(main())
"""
开始休眠 3 秒
开始休眠 3 秒
开始休眠 3 秒
休眠完成
休眠完成
休眠完成
"""
