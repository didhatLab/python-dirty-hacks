import asyncio
from asyncionotes.delay import delay


async def main():
    delay_task = asyncio.create_task(delay(3))

    try:
        res = await asyncio.wait_for(delay_task, timeout=2)
        print(res)
    except asyncio.TimeoutError:
        print("Got timeout")
        print(f"Task cancel status: {delay_task.cancelled()}")


asyncio.run(main())
