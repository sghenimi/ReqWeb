import asyncio


# define a coroutine
async def custom_coro():
    print("Asyncio 01")


# create the coroutine and run it in the event loop
asyncio.run(custom_coro())
