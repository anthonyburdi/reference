# Avoid deadlocks with a queue, which is thread-safe

import threading
import queue
import time

class Resource:
    def __init__(self):
        self.value = 0

    def increment(self):
        time.sleep(0.1)  # Simulate work
        self.value += 1

def worker(name, task_queue, resource):
    while True:
        try:
            task = task_queue.get(timeout=0.1)
            print(f"Worker {name} processing task {task}")
            resource.increment()
            task_queue.task_done()
        except queue.Empty:
            break
    print(f"Worker {name} finished")

if __name__ == "__main__":
    task_queue: queue.Queue = queue.Queue()
    shared_resource = Resource()
    num_tasks = 10
    num_workers = 3

    for i in range(num_tasks):
        task_queue.put(i)

    print("Queue:", list(task_queue.queue))

    threads = []
    for i in range(num_workers):
        thread = threading.Thread(target=worker, args=(f"Thread-{i}", task_queue, shared_resource))
        threads.append(thread)
        thread.start()

    task_queue.join()

    for thread in threads:
        thread.join()

    print(f"Final resource value: {shared_resource.value}")
