import asyncio
import time

async def myWork():
    print("Starting work")
    time.sleep(5)
    print("Finishing work")

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(myWork())
finally:
    loop.close()
