import threading, time

def task(name):
    print(f"Task {name} started")
    time.sleep(2)
    print(f"\nTask {name} completed")

thread1 = threading.Thread(target=task, args=("1",))
thread2 = threading.Thread(target=task, args=("2",))

thread1.start()
thread2.start()

thread1.join()
thread2.join()
