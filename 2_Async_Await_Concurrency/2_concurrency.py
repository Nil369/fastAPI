"""
Concurrency in FastAPI allows the application to handle multiple tasks at the same time,
even when some of them are waiting for external resources. This is different from parallelism.

- Concurrent Tasks:
  - Tasks switch context while waiting (e.g., for I/O operations).
  - Efficient for handling multiple requests in web servers.

- Parallel Tasks:
  - Tasks run simultaneously on different processors or threads.
  - Suitable for CPU-bound tasks (e.g., image processing).

---

### Concurrency Analogy: Burgers

Concurrent Burgers:
  - While waiting for burgers to cook, you talk to your crush (productive work).
  - Tasks switch attention between waiting and productive activities.

Parallel Burgers:
  - Multiple people cook burgers simultaneously.
  - Each person works on a different task, completing them faster.

For Web Applications:
- Concurrency (asynchronous operations) is often more efficient than parallelism
because most web tasks are I/O-bound.

---

### When to Use Async in FastAPI

1. Use `async def` if:
   - Your code uses libraries that support `await`.
   - Tasks are primarily I/O-bound (e.g., database calls, HTTP requests).

2. Use `def` if:
   - The libraries or tasks are not designed for async operations.
   - Your tasks are purely computational (CPU-bound).

---

### Performance Benefits

FastAPI leverages asynchronous programming to maximize efficiency:
- Handles I/O-bound tasks concurrently, reducing idle time.
- Supports parallelism for CPU-bound tasks if needed (e.g., with multiprocessing).

This makes FastAPI highly performant, comparable to Go and Node.js for web APIs.
"""

import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(1)
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())  # Run tasks concurrently

asyncio.run(main())
