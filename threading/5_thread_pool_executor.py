'''
    threading using concurrent library
'''

import concurrent.futures
import time

codeExecutionStartTime = time.perf_counter()


def task(timeToSleep):
    print("start code execution")
    print(f"code exectution will get stopped for {timeToSleep} sec")

    time.sleep(timeToSleep)

    # print("started executing again and task completed")
    return "started executing again and task completed"


# using context manager
with concurrent.futures.ThreadPoolExecutor() as executor:
    # it returns a future object => ie. to encapsulate the function passed inside
    # this future object is used to check in to the encapsulated function
    future_obj1 = executor.submit(task, 1.5)
    future_obj2 = executor.submit(task, 3)

    # .result() will wait until function completes
    print(future_obj1.result())
    print(future_obj1.result())

codeExecutionEndTime = time.perf_counter()
print(
    f"code execution start time is: {codeExecutionStartTime}\ncode execution end time is: {codeExecutionEndTime}\ntotal execution time: {codeExecutionEndTime-codeExecutionStartTime}")
