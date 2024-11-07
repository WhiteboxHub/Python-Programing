'''
Write a function that takes a number as an argument and returns its square.
'''
# def square(num):
#     return num * num

# # Test case
# print(square(4))  # Output: 16


'''
Write a function that takes two parameters, num and multiplier. Set multiplier's default value to 2 and return the product of both numbers.
'''

# def multiply(num, multiplier=2):
#     return num * multiplier

# # Test cases
# print(multiply(5))  # Output: 10 (uses default multiplier)
# print(multiply(5, 3))  # Output: 15 (uses provided multiplier)

'''
Write a function that takes a variable number of arguments and returns their sum.
'''
# def sum_numbers(*args):
#     return sum(args)

# # Test case
# print(sum_numbers(1, 2, 3, 4))  # Output: 10

'''
Write a function that accepts any number of keyword arguments and prints each key-value pair.
'''
# def print_info(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# # Test case
# print_info(name="Alice", age=30)  
# # Output:
# # name: Alice
# # age: 30

'''
Write a function that accepts both positional arguments and keyword arguments. 
The function should return a formatted string containing the name and age.
'''

# def greet(name, age, **kwargs):
#     return f"Hello {name}, you are {age} years old. Additional info: {kwargs}"

# # Test case
# print(greet("Bob", 25, city="New York", occupation="Engineer"))
# # Output: Hello Bob, you are 25 years old. Additional info: {'city': 'New York', 'occupation': 'Engineer'}

'''
Write a decorator that logs the execution of a function by printing a message before and after the function is called.
'''

# def log_decorator(func):
#     def wrapper(*args, **kwargs):
#         print(f"Calling {func.__name__}...")
#         result = func(*args, **kwargs)
#         print(f"{func.__name__} executed")
#         return result
#     return wrapper

# @log_decorator
# def add(a, b):
#     return a + b

# # Test case
# print(add(3, 4))  
# # Output:
# # Calling add...
# # add executed
# # 7

'''
Write a function outer that returns an inner function. The inner function should take a parameter and return its square.
'''
# def outer():
#     def inner(x):
#         return x * x
#     return inner

# # Test case
# square_func = outer()
# print(square_func(5))  # Output: 25

'''
Write a generator function count_up_to(n) that yields numbers from 1 to n.
'''




