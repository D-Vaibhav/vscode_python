import time
import threading

codeExecutionStartTime = time.perf_counter()


def task():
    print("start code execution")
    print("code exectution will get stopped for 3 sec")

    time.sleep(3)

    print("started executing again and task completed")


for _ in range(4):
    t = threading.Thread(target=task)
    t.start()
    # t.join()

codeExecutionEndTime = time.perf_counter()
print(
    f"code execution start time is: {codeExecutionStartTime}\ncode execution end time is: {codeExecutionEndTime}\ntotal execution time: {codeExecutionEndTime-codeExecutionStartTime}")
