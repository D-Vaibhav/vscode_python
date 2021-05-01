import time
import threading

codeExecutionStartTime = time.perf_counter()


def task(timeToSleep):
    print("start code execution")
    print(f"code exectution will get stopped for {timeToSleep} sec")

    time.sleep(timeToSleep)

    print("started executing again and task completed")


threads = []
for _ in range(4):
    # specifing for how long will task sleep in-between execution
    t = threading.Thread(target=task, args=[1.5])
    t.start()
    threads.append(t)

# for thread in threads:
#     thread.join()

codeExecutionEndTime = time.perf_counter()
print(
    f"code execution start time is: {codeExecutionStartTime}\ncode execution end time is: {codeExecutionEndTime}\ntotal execution time: {codeExecutionEndTime-codeExecutionStartTime}")
