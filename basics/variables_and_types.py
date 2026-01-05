"""
Variables and Data Types in Python
===================================
This module covers the basics of Python variables and data types.
Learning topics:
- Variable assignment
- Basic data types (int, float, str, bool)
- Collection types (list, tuple, dict, set)
- Type checking with type() and isinstance()
"""

# =============================================================================
# BASIC VARIABLES
# =============================================================================

# Assigning different types of values to variables
name = 'Ivan'  # String variable
surname = 'Lutso' 
age = 25       # Integer variable
height = 1.83  # Float variable
is_student = True  # Boolean variable

# Using f-string to format and print multiple variables
print(f'{name} {surname} is {age} years old, {height} meters tall, and student status is {is_student}.')


# =============================================================================
# PYTHON DATA TYPES
# =============================================================================

# Integer
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'>

# Float (decimal numbers)
my_float_var = 10.5
print(type(my_float_var))  # <class 'float'>

# String (text)
my_string_var = "Hello"
print(type(my_string_var))  # <class 'str'>

# Boolean (True/False)
my_boolean_var = False
print(type(my_boolean_var))  # <class 'bool'>

# Dictionary (key-value pairs)
my_dictionary_var = {"key": "value"}
print(type(my_dictionary_var))  # <class 'dict'>

# Tuple (immutable sequence)
my_tuple_var = (8, 4, 5)
print(type(my_tuple_var))  # <class 'tuple'>

# Range (sequence of numbers)
my_range_var = range(5)
print(type(my_range_var))  # <class 'range'>

# List (mutable sequence)
my_list_var = [2.3, 'Bye', 7, True]
print(type(my_list_var))  # <class 'list'>

# Set (unique elements)
my_set_var = {1, 2, 3}
print(type(my_set_var))  # <class 'set'>

# Bytes (immutable byte sequence)
my_bytes_var = b'example'
print(type(my_bytes_var))  # <class 'bytes'>

# Frozenset (immutable set)
my_frozenset_var = frozenset([4, 5, 6]) 
print(type(my_frozenset_var))  # <class 'frozenset'>

# Bytearray (mutable byte sequence)
my_bytearray_var = bytearray(b'example')
print(type(my_bytearray_var))  # <class 'bytearray'>

# Complex (complex numbers)
my_complex_var = 3 + 4j
print(type(my_complex_var))  # <class 'complex'>

# None (null value)
my_none_var = None
print(type(my_none_var))  # <class 'NoneType'>


# =============================================================================
# TYPE CHECKING WITH isinstance()
# =============================================================================

# isinstance() allows you to check if a variable is of a specific type
print(isinstance(age, int))      # True
print(isinstance('Cute', int))   # False
print(isinstance(height, float)) # True

print("End of variables_and_types.py")
