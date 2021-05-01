'''
    motive: to demostrate i/o operation causing delay via time.sleep()
    here code will wait to be executed at the times of sleep/waiting
'''

import time

codeExecutionStartTime = time.perf_counter()


def task():
    print("start code execution")
    print("code exectution will get stopped for 3 sec")

    # mimicking code is waiting for user input over here
    time.sleep(3)

    print("started executing again and task completed")


task()

codeExecutionEndTime = time.perf_counter()
print(
    f"code execution start time is: {codeExecutionStartTime}\ncode execution end time is: {codeExecutionEndTime}\ntotal execution time: {codeExecutionEndTime-codeExecutionStartTime}")
