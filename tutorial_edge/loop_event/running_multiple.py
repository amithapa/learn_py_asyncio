import asyncio

async def firstWorker():
    while True:
        await asyncio.sleep(1)
        print("First worker executed")

async def secondWorker():
    while True:
        await asyncio.sleep(1)
        print("Second worker executed")

loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(firstWorker())
    asyncio.ensure_future(secondWorker())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    loop.close()
    print("Loop closed")
