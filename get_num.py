import time
import asyncio

async def main1():
    print(f'{time.time()} Hello!')
    await asyncio.sleep(1.0)
    print(f'{time.time()} good bye!')

def blocking():
    time.sleep(0.5)
    print(f'{time.time()} from a thread!')

loop = asyncio.get_event_loop()
task1 = loop.create_task(main1())
task2 = loop.create_task(main1())

# loop.run_in_executor(None, blocking)
pending = [task1, task2]
group = asyncio.gather(*pending, return_exceptions=True)
print(group)
pending = asyncio.all_tasks(loop=loop)
for task in pending:
    task.cancel()

group = asyncio.gather(*pending, return_exceptions=True)
loop.run_until_complete(group)
loop.close()
