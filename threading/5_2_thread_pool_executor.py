'''
    before sleeping => order of code execution
    after sleeping => order of thread completion
'''

import concurrent.futures
import time

codeExecutionStartTime = time.perf_counter()


def task(timeToSleep):
    print(f"going to sleep for {timeToSleep} seconds")
    time.sleep(timeToSleep)

    return f"done sleeping for {timeToSleep} seconds"


with concurrent.futures.ThreadPoolExecutor() as tpExecutor:
    seconds = [4, 3, 2, 1]
    # creating list comprehension instead of using loop
    futureObjects = [tpExecutor.submit(task, sec) for sec in seconds]

    # to iterate over futureObjects
    for fo in concurrent.futures.as_completed(futureObjects):
        print(fo.result())

codeExecutionEndTime = time.perf_counter()
print(
    f"code execution start time is: {codeExecutionStartTime}\ncode execution end time is: {codeExecutionEndTime}\ntotal execution time: {codeExecutionEndTime-codeExecutionStartTime}")
