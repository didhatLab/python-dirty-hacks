import asyncio
from asyncionotes.delay import delay


async def main():
    long_task = asyncio.create_task(delay(10))

    second_sleep = 0

    while not long_task.done():
        print("Task not finish, check again second later")
        await asyncio.sleep(1)

        second_sleep += 1

        if second_sleep == 5:
            long_task.cancel()

    try:
        await long_task
    except asyncio.CancelledError:
        print("Task was canceled!")


asyncio.run(main())
