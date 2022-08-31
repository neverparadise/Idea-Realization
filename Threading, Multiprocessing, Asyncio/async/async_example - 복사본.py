# navtive coroutine
import asyncio
async def myfunc():
    print('Hellow World')

event_loop = asyncio.get_event_loop()
event_loop.run_until_complete(myfunc())
event_loop.close()

