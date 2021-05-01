import concurrent.futures
import time

codeExecutionStartTime = time.perf_counter()


def task(timeToSleep):
    print("start code execution")
    print(f"code exectution will get stopped for {timeToSleep} sec")

    time.sleep(timeToSleep)

    return "started executing again and task completed"


with concurrent.futures.ThreadPoolExecutor() as tpExecutor:
    # creating list comprehension instead of using loop
    futureObjects = [tpExecutor.submit(task, 1.5) for _ in range(7)]

    # to iterate over as per thread completion use : as_completed()
    for fo in concurrent.futures.as_completed(futureObjects):
        print(fo.result())

codeExecutionEndTime = time.perf_counter()
print(
    f"code execution start time is: {codeExecutionStartTime}\ncode execution end time is: {codeExecutionEndTime}\ntotal execution time: {codeExecutionEndTime-codeExecutionStartTime}")
