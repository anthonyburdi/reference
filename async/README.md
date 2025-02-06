# Async

Sandbox for async code experiments

Concurrency is the management of multiple tasks that overlap in execution, while parallelism is the execution of multiple tasks simultaneously.

## Libraries

- [asyncio](https://docs.python.org/3/library/asyncio.html) - Write concurrent code using the async/await syntax.
- [multiprocessing](https://docs.python.org/3/library/multiprocessing.html) - Multiple processes run in parallel, each with its own memory space and interpreter
- [threading](https://docs.python.org/3/library/threading.html) - Multiple threads in one process, sharing memory and resources.
- [Celery distributed task queue](https://github.com/celery/celery?tab=readme-ov-file) - Distributed task queue - run tasks asynchronously or in parallel across multiple nodes.
- NumPy/Pandas/Dask - Parallel computing e.g. ML, DataViz.
- Fast API/Flask - Web frameworks to handle multiple (stateless) requests concurrently.

## Reading

Some handy reading about concurrency / parallelism:

```
Modern versions of Python have support for "asynchronous code" using something called "coroutines", with async and await syntax.
```

- [Fast API Concurrency and async / await](https://fastapi.tiangolo.com/async/#concurrency-and-async-await)
- [Concurrency and Parallelism in Python: A brief introduction](https://medium.com/nerd-for-tech/concurrency-and-parallelism-in-python-a-brief-introduction-9fd19b8c6433)
- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)


# Multithreading vs. Multiprocessing

## **Multithreading**

### **Concept**
- Multiple threads run concurrently within the same process, sharing memory and resources.

### **Pros**
- Lightweight and faster to start than processes.
- Efficient for I/O-bound tasks (e.g., network requests, file operations) where threads can wait for I/O operations without blocking the entire process.

### **Cons**
- **Global Interpreter Lock (GIL):** In CPython, the GIL allows only one thread to execute Python bytecode at a time. This limits the performance gains of multithreading for CPU-bound tasks.
- More challenging to debug due to shared memory and potential race conditions.

---

## **Multiprocessing**

### **Concept**
- Multiple processes run in parallel, each with its own memory space and interpreter.

### **Pros**
- True parallelism, utilizing multiple CPU cores for CPU-bound tasks (e.g., complex calculations).
- Avoids the GIL limitations, enabling better performance for CPU-bound tasks.
- More resilient to errors, as a crash in one process doesn't affect others.

### **Cons**
- More overhead in terms of memory usage and process creation.
- Inter-process communication (IPC) is required to share data between processes.

---

## **When to Use**

### **I/O-bound tasks:**
- Use multithreading when your program spends a significant amount of time waiting for I/O operations.

### **CPU-bound tasks:**
- Use multiprocessing to take advantage of multiple cores for parallel processing.
