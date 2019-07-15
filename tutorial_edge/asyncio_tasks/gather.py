import asyncio

async def myWorker():
    print("Hello world")

async def main():
    print("My Main")

loop = asyncio.get_event_loop()

try:
    loop.run_until_complete(asyncio.gather(*[myWorker() for i in range(5)]))
except KeyboardInterrupt:
    pass
finally:
    loop.close()
