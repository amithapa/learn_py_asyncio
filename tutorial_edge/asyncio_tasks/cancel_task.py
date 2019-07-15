import asyncio
import time

async def myTask():
    time.sleep(1)
    print("Processing Task")

    for task in asyncio.Task.all_tasks():
        print(task)
        task.cancel()
        print(task)

async def myTaskGenerator():
    for i in range(5):
        asyncio.ensure_future(myTask())

loop = asyncio.get_event_loop()

loop.run_until_complete(myTaskGenerator())
print("All task has been completed!")
loop.close()
