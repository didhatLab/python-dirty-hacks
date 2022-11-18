import asyncio
import time


async def inner_test():
    print("sleep task for 2 seconds")
    await asyncio.sleep(2)


async def test_func():
    await inner_test()


funcs = [test_func for _ in range(10)]


async def main_with_gather():
    await asyncio.gather(*[f() for f in funcs])


async def main_without_gather():
    for f in funcs:
        await f()


async def main_with_tasks():
    for f in funcs:
        asyncio.create_task(f())


if __name__ == "__main__":
    start = time.time()
    loop = asyncio.new_event_loop()
    loop.run_until_complete(main_with_tasks())
    print(time.time() - start)

