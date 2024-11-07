'''
Write a program that simulates two tasks running concurrently, where one task takes 3 seconds and the other takes 2 seconds.

'''
# import asyncio

# async def task1():
#     print("Task 1 starting")
#     await asyncio.sleep(3)  # Simulate I/O operation
#     print("Task 1 finished")

# async def task2():
#     print("Task 2 starting")
#     await asyncio.sleep(2)  # Simulate I/O operation
#     print("Task 2 finished")

# # Run tasks concurrently
# async def main():
#     await asyncio.gather(task1(), task2())

# asyncio.run(main())

'''
Write a program that runs three tasks concurrently, each taking different amounts of time.
'''
# import asyncio

# async def task(name, seconds):
#     print(f"{name} starting")
#     await asyncio.sleep(seconds)  # Simulate I/O operation
#     print(f"{name} finished")

# async def main():
#     # Run three tasks concurrently
#     await asyncio.gather(
#         task("Task 1", 2),
#         task("Task 2", 3),
#         task("Task 3", 1)
#     )

# asyncio.run(main())

'''
Write a program that repeatedly prints "Hello" every 1 second for 5 seconds.
'''

# import asyncio

# async def greet():
#     for _ in range(5):
#         print("Hello")
#         await asyncio.sleep(1)  # Sleep for 1 second

# async def main():
#     await greet()

# asyncio.run(main())

'''
Write a program that times out a task if it takes longer than 2 seconds to complete.
'''

# import asyncio

# async def long_task():
#     print("Starting long task")
#     await asyncio.sleep(3)  # Simulate a long task
#     print("Long task finished")

# async def main():
#     try:
#         # Timeout after 2 seconds
#         await asyncio.wait_for(long_task(), timeout=2)
#     except asyncio.TimeoutError:
#         print("Task timed out!")

# asyncio.run(main())

'''
Write a program that uses an asynchronous context manager to simulate resource management.
'''
# import asyncio

# class AsyncResourceManager:
#     async def __aenter__(self):
#         print("Acquiring resource...")
#         await asyncio.sleep(1)  # Simulate resource acquisition
#         return "Resource"

#     async def __aexit__(self, exc_type, exc_val, exc_tb):
#         print("Releasing resource...")
#         await asyncio.sleep(1)  # Simulate resource release

# async def main():
#     async with AsyncResourceManager() as resource:
#         print(f"Using {resource}")

# asyncio.run(main())

'''
Write a program where one task waits for another task to complete before running.
'''

# import asyncio

# async def task1():
#     print("Task 1 starting")
#     await asyncio.sleep(2)
#     print("Task 1 finished")

# async def task2():
#     print("Task 2 starting")
#     await asyncio.sleep(1)
#     print("Task 2 finished")

# async def main():
#     await task1()  # Wait for task1 to finish before starting task2
#     await task2()

# asyncio.run(main())

'''
Write an asynchronous generator that yields numbers from 1 to 3, with a 1-second delay between each yield.
'''

# import asyncio

# async def number_generator():
#     for i in range(1, 4):
#         await asyncio.sleep(1)  # Simulate delay
#         yield i

# async def main():
#     async for number in number_generator():
#         print(f"Received number: {number}")

# asyncio.run(main())


'''
Write a program that simulates two tasks, one of which raises an exception, and handles both exceptions.
'''

# import asyncio

# async def task1():
#     print("Task 1 starting")
#     await asyncio.sleep(2)
#     raise ValueError("An error occurred in task 1")
#     print("Task 1 finished")

# async def task2():
#     print("Task 2 starting")
#     await asyncio.sleep(1)
#     print("Task 2 finished")

# async def main():
#     try:
#         await asyncio.gather(task1(), task2())
#     except ValueError as e:
#         print(f"Caught an exception: {e}")

# asyncio.run(main())

'''
    Write a program that runs multiple tasks concurrently using asyncio.create_task().
'''
# import asyncio

# async def task(name, delay):
#     print(f"{name} starting")
#     await asyncio.sleep(delay)
#     print(f"{name} finished")

# async def main():
#     task1 = asyncio.create_task(task("Task 1", 2))
#     task2 = asyncio.create_task(task("Task 2", 1))
    
#     await task1
#     await task2

# asyncio.run(main())



