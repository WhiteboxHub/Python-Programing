'''
Write a Python program to find the sum of all elements in a given list using a for loop.
'''
# def sum_of_elements(nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total

# # Test case
# nums = [1, 2, 3, 4, 5]
# print(sum_of_elements(nums))  # Output: 15


'''
Write a Python program to find the largest number in a given list using a for loop
'''

# def find_largest(nums):
#     largest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#     return largest

# # Test case
# nums = [1, 2, 3, 4, 5]
# print(find_largest(nums))  # Output: 5

'''
Write a Python program to count the occurrences of a given number in a list using a for loop.
'''

# def count_occurrences(nums, target):
#     count = 0
#     for num in nums:
#         if num == target:
#             count += 1
#     return count

# # Test case
# nums = [1, 2, 2, 3, 4, 2, 5]
# target = 2
# print(count_occurrences(nums, target))  # Output: 3


'''
Write a Python program to reverse a string using a for loop.
'''

# def reverse_string(s):
#     reversed_s = ""
#     for char in s:
#         reversed_s = char + reversed_s
#     return reversed_s

# # Test case
# s = "hello"
# print(reverse_string(s))  # Output: "olleh"

'''
rite a Python program to find all even numbers in a given list using a for loop.


'''
# def find_even_numbers(nums):
#     even_numbers = []
#     for num in nums:
#         if num % 2 == 0:
#             even_numbers.append(num)
#     return even_numbers

# # Test case
# nums = [1, 2, 3, 4, 5, 6]
# print(find_even_numbers(nums))  # Output: [2, 4, 6]

'''
    Write a Python program to check if a number is prime using a for loop.
'''

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, n):
#         if n % i == 0:
#             return False
#     return True

# # Test case
# n = 11
# print(is_prime(n))  # Output: True


'''
Write a Python program to print the Fibonacci series up to n terms using a for loop.
'''
# def fibonacci(n):
#     fib_series = []
#     a, b = 0, 1
#     for _ in range(n):
#         fib_series.append(a)
#         a, b = b, a + b
#     return fib_series

# # Test case
# n = 5
# print(fibonacci(n))  # Output: [0, 1, 1, 2, 3]
