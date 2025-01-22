"""

FastAPI utilizes Python's `async` and `await` syntax to handle asynchronous programming
effectively.This approach is particularly valuable for web applications, where many
operations involve waiting (e.g., I/O operations such as database queries,
API requests, or file reading). Here's a breakdown of the key concepts:

---
1. Async and Await

What is `async`?
  - Declares a function as asynchronous, enabling it to handle I/O operations without blocking the main execution thread.
  - These functions are defined using `async def`.

What is `await`?
  - Suspends the execution of the async function until the awaited task is completed.
  - Can only be used inside functions declared with `async def`.

**Example:**
```python
@app.get('/')
async def read_results():
    results = await some_library()  # Suspends until some_library() completes.
    return results
```

**Key Points:**
- You must use `await` with functions or libraries that support asynchronous operations.
- Typical use cases involve waiting for I/O-bound tasks.

---

### **2. Def Functions vs. Async Functions**

- **Def Functions:**
  - Used for synchronous operations.
  - Suitable for libraries or tasks that do not support `await`.

- **Async Functions:**
  - Used for asynchronous operations.
  - Ideal for I/O-bound tasks where waiting is required.

**Mixing Synchronous and Asynchronous:**
FastAPI allows you to mix both `def` and `async def` in your path operations, optimizing performance based on the nature of the tasks.

**Example:**
```python
@app.get('/sync')
def get_sync_results():
    return some_library()  # Synchronous call.

@app.get('/async')
async def get_async_results():
    return await some_async_library()  # Asynchronous call.
```
"""

async def my_async_function():
    print("Hello, Async!")


# ********* asyncio module **********
import asyncio

async def fetch_data():
    print("Fetching data...")
    await asyncio.sleep(2)  # Simulates a delay
    print("Data fetched")

asyncio.run(fetch_data())
