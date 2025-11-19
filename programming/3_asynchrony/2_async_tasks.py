import time
import asyncio


async def do_async_task(n):
    print(f"# start task {n}")
    await asyncio.sleep(2)
    print(f"# End task {n}")


async def main():
    start = time.perf_counter()
    await asyncio.gather(do_async_task(1), do_async_task(2))
    end = time.perf_counter()
    print(f"--> Taken : {end-start}")


asyncio.run(main())

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(do_async_task(1), do_async_task(2)))
