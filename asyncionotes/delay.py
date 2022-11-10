import asyncio


async def delay(seconds: int):
    print(f"Start task for sleep {seconds} second(s)")
    await asyncio.sleep(seconds)
    print(f"End tasks for sleep {seconds} second(s)")

