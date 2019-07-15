import asyncio

async def myCoroutine():
    print("Simple Event Loop Example")

def main():
    # Define an instance of event loop
    loop = asyncio.get_event_loop()

    loop.run_until_complete(myCoroutine())

    loop.close()

if __name__ == "__main__":
    main()
