import asyncio
import time

async def myTask():
    time.sleep(1)
    print("Processing Task,")

async def myTaskGenerator():
    for i in range(5):
        asyncio.ensure_future(myTask())
    pending = asyncio.Task.all_tasks()
    print(pending)

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(myTaskGenerator())
    print("Completed All tasks")
finally:
    loop.close()
