
async def sync_context_manager_for_file():

    async with open("test.txt", mode="w"):
        pass
