import asyncio


async def myWorker(semaphore, sleep_time):
    await semaphore.acquire()
    print(f"Successfully acquired the semaphore {sleep_time}")
    await asyncio.sleep(sleep_time)
    print(f"Releasing semaphore {sleep_time}")
    semaphore.release()

async def main():
    mySemaphore = asyncio.Semaphore(value=2)
    await asyncio.wait([myWorker(mySemaphore, 8), myWorker(mySemaphore,3), myWorker(mySemaphore,3)])
    print("Main Coroutine")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
print("All workers completed.")
loop.close()
