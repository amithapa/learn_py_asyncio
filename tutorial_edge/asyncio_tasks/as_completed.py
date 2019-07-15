import asyncio

async def myWorker(number):
    return number * 2

async def main(coros):
    for fs in asyncio.as_completed(coros):
        print(await fs)

coros = [myWorker(i) for i in range(5)]

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(main(coros))
except KeyboardInterrupt:
    pass
finally:
    loop.close()
