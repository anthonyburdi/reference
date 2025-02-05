import asyncio

async def fetch_data(url):
    print(f"Start fetching data from {url}")
    await asyncio.sleep(2)
    print(f"Done fetching data from {url}")
    return {"data": f"Data from {url}"}

async def main():
    tasks = [fetch_data("url1"), fetch_data("url2"), fetch_data("url3")]
    results = await asyncio.gather(*tasks)
    print(results)

if __name__ == '__main__':
    asyncio.run(main())
