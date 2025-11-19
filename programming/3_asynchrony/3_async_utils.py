import aiohttp
import asyncio


async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://jsonplaceholder.typicode.com/posts/2",
        "https://jsonplaceholder.typicode.com/posts/3",
        "https://jsonplaceholder.typicode.com/posts/4",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        responses = await asyncio.gather(*tasks)

        for i, response in enumerate(responses):
            print(
                f"Response {i+1}: {response}..."
            )  # Print first 60 characters of each response


# Run the event loop
asyncio.run(main())
