'''
    why thrread: so code will start executing async. whenever waiting
'''
import time
import threading

codeExecutionStartTime = time.perf_counter()


def task():
    print("start code execution")
    print("code exectution will get stopped for 3 sec")

    # mimicking code is waiting for user input over here
    time.sleep(3)

    print("started executing again and task completed")


# creting threads for tasks
t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

# running thread
t1.start()
t2.start()

# join will disable threading capabilities of a thread
# just for demonstration purpose
t1.join()
t2.join()

codeExecutionEndTime = time.perf_counter()
print(
    f"code execution start time is: {codeExecutionStartTime}\ncode execution end time is: {codeExecutionEndTime}\ntotal execution time: {codeExecutionEndTime-codeExecutionStartTime}")
