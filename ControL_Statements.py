'''

Write a program that takes a number as input and checks if it's a prime number.
A prime number is only divisible by 1 and itself.

'''

# def is_prime(n):
#     if n <= 1:
#         return False  # Numbers less than or equal to 1 are not prime
    
#     for i in range(2, n):
#         if n % i == 0:
#             return False  # If divisible by any number other than 1 and itself, it's not prime
#     return True

# # Test the function
# number = int(input("Enter a number: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")

'''

Write a program to count the number of vowels (a, e, i, o, u) in a given string.

'''

# def count_vowels(string):
#     count = 0
#     for char in string:
#         if char in 'aeiouAEIOU':
#             count += 1
#     return count

# # Test the function
# input_string = input("Enter a string: ")
# print(f"Number of vowels: {count_vowels(input_string)}")


'''

Write a program that prints a triangle pattern using numbers, where each row contains increasing numbers up to the row number.

'''

# def print_triangle(n):
#     for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print(j, end=" ")
#         print()

# # Test the function
# rows = int(input("Enter number of rows: "))
# print_triangle(rows)


'''

Write a program that calculates the factorial of a given number using a loop. 

'''

# def factorial(n):
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result

# # Test the function
# number = int(input("Enter a number: "))
# print(f"Factorial of {number} is: {factorial(number)}")


'''
Write a program to find the largest element in a list of integers.

'''

# def find_largest(nums):
#     largest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#     return largest

# # Test the function
# numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
# print(f"The largest number is: {find_largest(numbers)}")


'''
Write a program to find the largest element in a list of integers.

'''

# def find_largest(nums):
#     largest = nums[0]
#     for num in nums:
#         if num > largest:
#             largest = num
#     return largest

# # Test the function
# numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
# print(f"The largest number is: {find_largest(numbers)}")


