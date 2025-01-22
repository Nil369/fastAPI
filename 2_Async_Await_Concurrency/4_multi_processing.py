from multiprocessing import Process
import time

def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"Task {name} completed")

process1 = Process(target=task, args=("1",))
process2 = Process(target=task, args=("2",))

process1.start()
process2.start()

process1.join()
process2.join()
