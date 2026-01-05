"""
Strings and String Formatting in Python
========================================
This module covers string operations and formatting in Python.
Learning topics:
- String methods (upper, lower, replace, split)
- String slicing
- String concatenation
- The 'in' operator for substrings
- String length with len()
- Print function with custom separators
"""

# =============================================================================
# PRINT FUNCTION WITH SEPARATOR
# =============================================================================

# Demonstrating the use of the sep parameter in the print function
# to customize the separator between printed items
print('My favorite drinks are', 'red bull', 'Fritz Cola', 'and', 'coffee.', sep=' > ')


# =============================================================================
# STRING OPERATIONS
# =============================================================================

# Using the 'in' operator to check for substring presence in a string
test_str = 'Hi there!'
print('Hi' in test_str)      # True
print('hello' in test_str)   # False (case-sensitive!)

# String manipulation examples
my_str = "If Python was an AI, bubble would never have existed."

# Getting the length of the string
print(len(my_str))

# Converting string to uppercase
my_str = my_str.upper()

# Slicing the string from index 3 to 9 (9 is exclusive)
print(my_str[3:9])

# Replacing a substring in the string
print(my_str.replace('PYTHON', 'JavaScript'))

# Splitting the string into a list based on a delimiter
print(my_str.split(','))


# =============================================================================
# STRING CONCATENATION
# =============================================================================

# Creating two string variables
my_str_draft = "No matter where you live"
my_str_final = ", matter what inside your code." 

# Concatenating two strings using the + operator
concat = my_str_draft + my_str_final
print(concat)

# Repeating a string using the * operator
print(concat + " " * 3)

print("End of strings_and_formatting.py")
