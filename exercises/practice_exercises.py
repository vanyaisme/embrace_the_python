"""
Python Practice Exercises
==========================
This file contains beginner-friendly Python exercises to practice fundamental concepts.

Instructions:
- Read each exercise carefully
- Try to solve it on your own first
- Example solutions are provided at the bottom (commented out)
- Uncomment solutions to check your work
"""

# =============================================================================
# EXERCISE 1: FizzBuzz
# =============================================================================
"""
Write a program that prints numbers from 1 to 20.
For multiples of 3, print "Fizz" instead of the number.
For multiples of 5, print "Buzz" instead of the number.
For multiples of both 3 and 5, print "FizzBuzz".

Example output:
1
2
Fizz
4
Buzz
Fizz
...
"""

# Your solution here:


# =============================================================================
# EXERCISE 2: Palindrome Checker
# =============================================================================
"""
Write a function that checks if a given string is a palindrome.
A palindrome is a word that reads the same backward as forward.

Examples:
- "racecar" -> True
- "hello" -> False
- "madam" -> True
"""

# Your solution here:
# def is_palindrome(text):
#     pass


# =============================================================================
# EXERCISE 3: Sum Calculator
# =============================================================================
"""
Write a function that takes a list of numbers and returns their sum.
Don't use the built-in sum() function.

Example:
- calculate_sum([1, 2, 3, 4, 5]) -> 15
- calculate_sum([10, 20, 30]) -> 60
"""

# Your solution here:
# def calculate_sum(numbers):
#     pass


# =============================================================================
# EXERCISE 4: Find Maximum
# =============================================================================
"""
Write a function that finds the maximum number in a list.
Don't use the built-in max() function.

Example:
- find_max([3, 7, 2, 9, 1]) -> 9
- find_max([15, 8, 23, 4]) -> 23
"""

# Your solution here:
# def find_max(numbers):
#     pass


# =============================================================================
# EXERCISE 5: Count Vowels
# =============================================================================
"""
Write a function that counts the number of vowels (a, e, i, o, u) in a string.
Make it case-insensitive.

Example:
- count_vowels("Hello World") -> 3
- count_vowels("Python Programming") -> 5
"""

# Your solution here:
# def count_vowels(text):
#     pass


# =============================================================================
# EXERCISE 6: Reverse String
# =============================================================================
"""
Write a function that reverses a string without using built-in reverse methods.

Example:
- reverse_string("hello") -> "olleh"
- reverse_string("Python") -> "nohtyP"
"""

# Your solution here:
# def reverse_string(text):
#     pass


# =============================================================================
# EXERCISE 7: Even or Odd Counter
# =============================================================================
"""
Write a function that takes a list of numbers and returns a dictionary
with the count of even and odd numbers.

Example:
- count_even_odd([1, 2, 3, 4, 5, 6]) -> {"even": 3, "odd": 3}
- count_even_odd([2, 4, 6, 8]) -> {"even": 4, "odd": 0}
"""

# Your solution here:
# def count_even_odd(numbers):
#     pass


# =============================================================================
# EXERCISE 8: Temperature Converter
# =============================================================================
"""
Write two functions:
1. celsius_to_fahrenheit(celsius) - converts Celsius to Fahrenheit
2. fahrenheit_to_celsius(fahrenheit) - converts Fahrenheit to Celsius

Formulas:
- F = (C * 9/5) + 32
- C = (F - 32) * 5/9

Example:
- celsius_to_fahrenheit(0) -> 32.0
- fahrenheit_to_celsius(32) -> 0.0
"""

# Your solution here:
# def celsius_to_fahrenheit(celsius):
#     pass

# def fahrenheit_to_celsius(fahrenheit):
#     pass


# =============================================================================
# EXERCISE 9: List Duplicates Remover
# =============================================================================
"""
Write a function that removes duplicates from a list while maintaining order.

Example:
- remove_duplicates([1, 2, 2, 3, 4, 4, 5]) -> [1, 2, 3, 4, 5]
- remove_duplicates(['a', 'b', 'a', 'c']) -> ['a', 'b', 'c']
"""

# Your solution here:
# def remove_duplicates(items):
#     pass


# =============================================================================
# EXERCISE 10: Factorial Calculator
# =============================================================================
"""
Write a function that calculates the factorial of a number.
Factorial of n (n!) is the product of all positive integers less than or equal to n.

Example:
- factorial(5) -> 120 (5 * 4 * 3 * 2 * 1)
- factorial(3) -> 6 (3 * 2 * 1)
- factorial(0) -> 1 (by definition)
"""

# Your solution here:
# def factorial(n):
#     pass


# =============================================================================
# EXAMPLE SOLUTIONS (COMMENTED OUT)
# =============================================================================
"""
Uncomment these solutions to check your work or if you get stuck!

# SOLUTION 1: FizzBuzz
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# SOLUTION 2: Palindrome Checker
def is_palindrome(text):
    text = text.lower()
    return text == text[::-1]

# Test
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False


# SOLUTION 3: Sum Calculator
def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Test
print(calculate_sum([1, 2, 3, 4, 5]))  # 15


# SOLUTION 4: Find Maximum
def find_max(numbers):
    if not numbers:
        return None
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# Test
print(find_max([3, 7, 2, 9, 1]))  # 9


# SOLUTION 5: Count Vowels
def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

# Test
print(count_vowels("Hello World"))  # 3


# SOLUTION 6: Reverse String
def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text

# Test
print(reverse_string("hello"))  # "olleh"


# SOLUTION 7: Even or Odd Counter
def count_even_odd(numbers):
    even_count = 0
    odd_count = 0
    for num in numbers:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    return {"even": even_count, "odd": odd_count}

# Test
print(count_even_odd([1, 2, 3, 4, 5, 6]))  # {"even": 3, "odd": 3}


# SOLUTION 8: Temperature Converter
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test
print(celsius_to_fahrenheit(0))    # 32.0
print(fahrenheit_to_celsius(32))   # 0.0


# SOLUTION 9: List Duplicates Remover
def remove_duplicates(items):
    seen = []
    for item in items:
        if item not in seen:
            seen.append(item)
    return seen

# Test
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))  # [1, 2, 3, 4, 5]


# SOLUTION 10: Factorial Calculator
def factorial(n):
    if n == 0 or n == 1:
        return 1
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Test
print(factorial(5))  # 120
print(factorial(3))  # 6
print(factorial(0))  # 1
"""
