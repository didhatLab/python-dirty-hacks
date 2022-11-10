import asyncio
from asyncionotes.delay import delay


async def main():
    sleep_for_three = asyncio.create_task(delay(3))
    sleep_again = asyncio.create_task(delay(3))
    sleep_more = asyncio.create_task(delay(3))

    await sleep_for_three
    await sleep_again
    await sleep_more


asyncio.run(main())
