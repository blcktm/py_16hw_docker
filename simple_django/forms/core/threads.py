import time
# import threading
# import multiprocessing
import asyncio
# import sys

COUNTS = 90000000


async def count_me(count):
    while count > 0:
        count -= 1
        # print(count)


# async def main(loop):
async def main():
    # loop.create_task(count_me(COUNTS / 3))
    # loop.create_task(count_me(COUNTS / 3))
    # loop.create_task(count_me(COUNTS / 3))
    tasks = [
        asyncio.ensure_future(count_me(COUNTS / 3)),
        asyncio.ensure_future(count_me(COUNTS / 3)),
        asyncio.ensure_future(count_me(COUNTS / 3))
    ]
    # return await asyncio.gather(*tasks)
    return await asyncio.wait(tasks)

t1 = time.time()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
# loop.run_until_complete(main(loop))

print(time.time() - t1)

# async def main(task_count):
#     # loop = asyncio.get_event_loop()
#     for x in range(0, task_count):
#         # loop.create_task(count_me(COUNTS / task_count))
#         asyncio.create_task(count_me(COUNTS / task_count))
#
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(main(3))
# t1 = time.time()
# asyncio.run(main(3))
# print(time.time() - t1)

# COUNTS = []
# b = COUNTS.copy()
# print(sys.getrefcount(b))
# sys.setcheckinterval(1000)
# print(sys.getcheckinterval())

# def count_me(count):
#     while count > 0:
#         count -= 1
#
#
# def main(count):
#     print('Main start')
#     while count > 0:
#         count -= 1
#
#     process1 = multiprocessing.Process(target=count_me, args=(count / 3,))
#     process2 = multiprocessing.Process(target=count_me, args=(count / 3,))
#     process3 = multiprocessing.Process(target=count_me, args=(count / 3,))
#
#     process1.start()
#     process2.start()
#     process3.start()
#
#     process1.join()
#     process2.join()
#     process3.join()
#
#
# if __name__ == '__main__':
#     t1 = time.time()
#
#     process1 = multiprocessing.Process(target=main, args=(COUNTS / 3,))
#     process2 = multiprocessing.Process(target=main, args=(COUNTS / 3,))
#     process3 = multiprocessing.Process(target=main, args=(COUNTS / 3,))
#
#     process1.start()
#     process2.start()
#     process3.start()
#
#
#
#     # TODO Threading
#     # thread1 = threading.Thread(target=main, args=(COUNTS / 2,))
#     # thread2 = threading.Thread(target=main, args=(COUNTS / 2,))
#     #
#     # thread1.start()
#     # thread2.start()
#     #
#     # thread1.join()
#     # thread2.join()
#
#     # main(COUNTS / 2)
#     # main(COUNTS / 2)
#     process1.join()
#     print(time.time() - t1)
#     process2.join()
#     print(time.time() - t1)
#     process3.join()
#     print(time.time() - t1)
