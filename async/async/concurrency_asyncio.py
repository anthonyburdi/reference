import asyncio
import time

async def fetch_data(url):
    print(f"Start fetching data from {url}")
    await asyncio.sleep(2)
    print(f"Done fetching data from {url}")
    return {"data": f"Data from {url}"}

async def main():
    start = time.perf_counter()

    # Batch: Create tasks and then gather example:
    batch_tasks = [fetch_data("url1"), fetch_data("url2"), fetch_data("url3")]
    results = await asyncio.gather(*batch_tasks)
    print(results)
    end = time.perf_counter()
    elapsed = end - start
    print(f"Elapsed time: {elapsed:2f}")

    # Alternative batch config (note await on batch_tasks)
    batch_tasks = asyncio.gather(fetch_data("url4"), fetch_data("url5"))
    res1, res2 = await batch_tasks
    print(res1, res2)
    end2 = time.perf_counter()
    elapsed2 = end2 - end
    print(f"Elapsed time: {elapsed2:2f}")

    # Create task for each coroutine, await individually
    url1 = asyncio.create_task(fetch_data("create_task_url_1"))
    url2 = asyncio.create_task(fetch_data("create_task_url_2"))
    res_url_1 = await url1
    res_url_2 = await url2
    print(res_url_1, res_url_2)
    end3 = time.perf_counter()
    elapsed3 = end3 - end2
    print(f"Elapsed time: {elapsed3:2f}")


if __name__ == '__main__':
    asyncio.run(main())
