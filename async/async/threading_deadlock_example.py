"""
In this example, if thread A acquires lock_a and thread B acquires lock_b simultaneously, they will both be blocked indefinitely, waiting for each other to release the other lock, resulting in a deadlock.

Output:
Thread A acquired lock_a
Thread B acquired lock_b
<program hangs due to deadlock>
"""

import threading
import time

lock_a = threading.Lock()
lock_b = threading.Lock()

def thread_a():
    with lock_a:
        print("Thread A acquired lock_a")
        time.sleep(1)
        with lock_b:
            print("Thread A acquired lock_b")
    print("Thread A finished")

def thread_b():
    with lock_b:
        print("Thread B acquired lock_b")
        time.sleep(1)
        with lock_a:
            print("Thread B acquired lock_a")
    print("Thread B finished")

if __name__ == "__main__":
    thread1 = threading.Thread(target=thread_a)
    thread2 = threading.Thread(target=thread_b)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Main thread finished")