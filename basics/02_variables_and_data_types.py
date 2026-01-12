# =============================================================================
# VARIABLES AND DATA TYPES
# =============================================================================
# This module covers Python's variable system and built-in data types:
# - Variable declaration and assignment
# - Python's built-in data types (numeric, text, boolean, sequences, mappings, sets, binary)
# - Type checking with isinstance()
# - Membership testing with 'in' operator


# -----------------------------------------------------------------------------
# 1. VARIABLES AND DATA TYPES
# -----------------------------------------------------------------------------
# Variables are containers for storing data values.
# Python is dynamically typed - you don't need to declare the type explicitly.

# Example: Storing personal information in variables
name = 'Ivan'
surname = 'Lutso'
age = 25
height = 1.83
is_student = True

# Using f-string to format and display multiple variables
print(f'{name} {surname} is {age} years old, {height} meters tall, and student status is {is_student}.')
# Output: Ivan Lutso is 25 years old, 1.83 meters tall, and student status is True.


# -----------------------------------------------------------------------------
# 2. PYTHON'S BUILT-IN DATA TYPES
# -----------------------------------------------------------------------------
# Python has many built-in data types. Each type serves different purposes.
# Use the type() function to check the type of any object.

# NUMERIC TYPES
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'> - Whole numbers

my_float_var = 10.5
print(type(my_float_var))  # <class 'float'> - Decimal numbers

my_complex_var = 3 + 4j
# <class 'complex'> - Complex numbers with real and imaginary parts
print(type(my_complex_var))

# TEXT TYPE
my_string_var = "Hello"
print(type(my_string_var))  # <class 'str'> - Sequence of characters

# BOOLEAN TYPE
my_boolean_var = False
print(type(my_boolean_var))  # <class 'bool'> - True or False values

# SEQUENCE TYPES
my_list_var = [2.3, 'Bye', 7, True]
print(type(my_list_var))  # <class 'list'> - Ordered, mutable collection

my_tuple_var = (8, 4, 5)
print(type(my_tuple_var))  # <class 'tuple'> - Ordered, immutable collection

my_range_var = range(5)
print(type(my_range_var))  # <class 'range'> - Sequence of numbers (0 to 4)

# MAPPING TYPE
my_dictionary_var = {"key": "value"}
print(type(my_dictionary_var))  # <class 'dict'> - Key-value pairs

# SET TYPES
my_set_var = {1, 2, 3}
print(type(my_set_var))  # <class 'set'> - Unordered collection of unique items

my_frozenset_var = frozenset([4, 5, 6])
print(type(my_frozenset_var))  # <class 'frozenset'> - Immutable set

# BINARY TYPES
my_bytes_var = b'example'
print(type(my_bytes_var))  # <class 'bytes'> - Immutable sequence of bytes

my_bytearray_var = bytearray(b'example')
# <class 'bytearray'> - Mutable sequence of bytes
print(type(my_bytearray_var))

# NONE TYPE
my_none_var = None
print(type(my_none_var))  # <class 'NoneType'> - Represents absence of value


# -----------------------------------------------------------------------------
# 3. TYPE CHECKING WITH isinstance()
# -----------------------------------------------------------------------------
# The isinstance() function checks if an object is an instance of a specific type.
# Returns True or False. More flexible than type() for type checking.
# Syntax: isinstance(object, type)

print(isinstance(age, int))           # True - age is an integer
# False - 'Cute' is a string, not an integer
print(isinstance('Cute', int))
print(isinstance(height, float))      # True - height is a float
print(isinstance(is_student, bool))   # True - is_student is a boolean


# -----------------------------------------------------------------------------
# 4. MEMBERSHIP TESTING WITH 'in' OPERATOR
# -----------------------------------------------------------------------------
# The 'in' operator checks if a value exists within a sequence (string, list, etc.).
# Returns True if found, False otherwise.

test_str = 'Hi there!'
print('Hi' in test_str)       # True - 'Hi' is present in the string
# False - 'hello' is not present (case-sensitive!)
print('hello' in test_str)
print('there' in test_str)    # True - 'there' is present


print("\n" + "="*60)
print("END OF VARIABLES AND DATA TYPES MODULE")
print("="*60 + "\n")
