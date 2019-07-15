import asyncio

async def myWork():
    while True:
        await asyncio.sleep(1)
        print("Task executed")

loop = asyncio.get_event_loop()

try:
    asyncio.ensure_future(myWork())
    loop.run_forever()
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
