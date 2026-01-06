# =============================================================================
# SESSION 1: 05/01/2026 — PYTHON FUNDAMENTALS
# =============================================================================
# This session covers the core building blocks of Python programming:
# basic I/O, functions, variables, data types, and introductory string operations.


# -----------------------------------------------------------------------------
# 1. BASIC OUTPUT WITH print()
# -----------------------------------------------------------------------------
# The print() function displays output to the console/terminal.
# It's one of the most fundamental functions in Python.

print("Hello World!")  # Output: Hello World!


# -----------------------------------------------------------------------------
# 2. FUNCTIONS - DEFINING AND CALLING
# -----------------------------------------------------------------------------
# Functions are reusable blocks of code that perform specific tasks.
# Syntax: def function_name(parameters):
#            code block
# Functions help organize code and avoid repetition.

def greet(name):
    # This function takes one input (name) and prints a greeting message
    # The 'name' parameter is the value passed when calling the function
    print(f'Hello, {name}!')


# Calling the function with an argument
greet("Alice")  # Output: Hello, Alice!


# -----------------------------------------------------------------------------
# 3. ADVANCED print() FEATURES
# -----------------------------------------------------------------------------
# The print() function accepts multiple arguments and various parameters.

# Using the sep parameter to customize the separator between items
# Default separator is a space (' '), but you can change it to any string
print('My favorite drinks are', 'red bull', 'Fritz Cola', 'and', 'coffee.', sep=' > ')
# Output: My favorite drinks are > red bull > Fritz Cola > and > coffee.


# -----------------------------------------------------------------------------
# 4. VARIABLES AND DATA TYPES
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
# 5. PYTHON'S BUILT-IN DATA TYPES
# -----------------------------------------------------------------------------
# Python has many built-in data types. Each type serves different purposes.
# Use the type() function to check the type of any object.

# NUMERIC TYPES
my_integer_var = 10
print(type(my_integer_var))  # <class 'int'> - Whole numbers

my_float_var = 10.5
print(type(my_float_var))  # <class 'float'> - Decimal numbers

my_complex_var = 3 + 4j
print(type(my_complex_var))  # <class 'complex'> - Complex numbers with real and imaginary parts

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
print(type(my_bytearray_var))  # <class 'bytearray'> - Mutable sequence of bytes

# NONE TYPE
my_none_var = None
print(type(my_none_var))  # <class 'NoneType'> - Represents absence of value


# -----------------------------------------------------------------------------
# 6. TYPE CHECKING WITH isinstance()
# -----------------------------------------------------------------------------
# The isinstance() function checks if an object is an instance of a specific type.
# Returns True or False. More flexible than type() for type checking.
# Syntax: isinstance(object, type)

print(isinstance(age, int))           # True - age is an integer
print(isinstance('Cute', int))        # False - 'Cute' is a string, not an integer
print(isinstance(height, float))      # True - height is a float
print(isinstance(is_student, bool))   # True - is_student is a boolean


# -----------------------------------------------------------------------------
# 7. MEMBERSHIP TESTING WITH 'in' OPERATOR
# -----------------------------------------------------------------------------
# The 'in' operator checks if a value exists within a sequence (string, list, etc.).
# Returns True if found, False otherwise.

test_str = 'Hi there!'
print('Hi' in test_str)       # True - 'Hi' is present in the string
print('hello' in test_str)    # False - 'hello' is not present (case-sensitive!)
print('there' in test_str)    # True - 'there' is present


# -----------------------------------------------------------------------------
# 8. BASIC STRING OPERATIONS
# -----------------------------------------------------------------------------
# Strings are sequences of characters and support many useful operations.

my_str = "If Python was an AI, bubble would never have existed."

# Get string length
print(f'Length of string: {len(my_str)}')  # Output: Length of string: 55

# Convert to uppercase (returns a new string, doesn't modify original)
my_str = my_str.upper()
print(my_str)  # Output: IF PYTHON WAS AN AI, BUBBLE WOULD NEVER HAVE EXISTED.

# String slicing - extract substring from index 3 to 8 (9 is excluded)
print(my_str[3:9])  # Output: PYTHON

# Replace substring with another
print(my_str.replace('PYTHON', 'JavaScript'))  
# Output: IF JavaScript WAS AN AI, BUBBLE WOULD NEVER HAVE EXISTED.

# Split string into a list at comma delimiter
print(my_str.split(','))  
# Output: ['IF PYTHON WAS AN AI', ' BUBBLE WOULD NEVER HAVE EXISTED.']


# -----------------------------------------------------------------------------
# 9. STRING CONCATENATION AND REPETITION
# -----------------------------------------------------------------------------
# Strings can be combined using the + operator (concatenation)
# and repeated using the * operator.

my_str_draft = "No matter where you live"
my_str_final = ", matter what inside your code."

# Concatenate two strings
concat = my_str_draft + my_str_final
print(concat)  # Output: No matter where you live, matter what inside your code.

# Repeat a string multiple times using *
print((concat + " ") * 3)  # Repeats the string 3 times with a space after each


print("\n" + "="*60)
print("END OF SESSION 1")
print("="*60 + "\n")


# =============================================================================
# SESSION 2: 06/01/2026 - ADVANCED STRING OPERATIONS
# =============================================================================

# -----------------------------------------------------------------------------
# 1. STRING CONCATENATION AND TYPE CONVERSION
# -----------------------------------------------------------------------------
# In Python, you can only concatenate strings with other strings.
# To combine strings with other data types, you must first convert them to strings.

name_str = "Alex"
age_integer = 30

# Method 1: Using str() function to convert integer to string before concatenation
print(name_str + str(age_integer))  # Output: Alex30

# Method 2: Using the += operator for concatenation
name_and_age = name_str
name_and_age += str(age_integer)  # Same as: name_and_age = name_and_age + str(age_integer)
print(name_and_age)  # Output: Alex30


# -----------------------------------------------------------------------------
# 2. STRING FORMATTING WITH F-STRINGS
# -----------------------------------------------------------------------------
# F-strings (formatted string literals) provide a clean way to embed expressions
# inside strings. They're prefixed with 'f' or 'F' and use curly braces {} to
# insert variables and expressions. This is called "string interpolation".

# Basic f-string usage
greeting = f'Hello, my name is {name_str} and I am {age_integer} years old.'
print(greeting)  # Output: Hello, my name is Alex and I am 30 years old.

# Embedding expressions directly in f-strings (no need for str() conversion!)
num1 = 20
num2 = 8
print(f'The sum of {num1} and {num2} is {num1 + num2}.')  # Output: The sum of 20 and 8 is 28.


# -----------------------------------------------------------------------------
# 3. STRING SLICING AND INDEXING
# -----------------------------------------------------------------------------
# String slicing allows you to extract portions of a string using the syntax:
# string[start:end:step]
# - start: beginning index (inclusive)
# - end: ending index (exclusive)
# - step: increment between characters (default is 1)
# Important: Strings are immutable - slicing creates a new string, doesn't modify the original

sample_str = "The Earth orbits the Sun in an elliptical path."

# Basic slicing - extract characters from index 4 to 24
print(sample_str[4:25])  # Output: Earth orbits the Sun

# Omitting start or end indices
print(sample_str[:10])   # From start to index 9: The Earth
print(sample_str[11:])   # From index 11 to end: orbits the Sun in an elliptical path.

# Using step to skip characters
print(sample_str[0:25:2])  # Every 2nd character from 0 to 24: TeErhobt h u

# Negative step to reverse the string
print(sample_str[::-1])  # Output: .htap lacitpille na ni nuS eht stibro htraE ehT


# -----------------------------------------------------------------------------
# 4. STRING CASE TRANSFORMATION METHODS
# -----------------------------------------------------------------------------
# Python provides several methods to change the capitalization of strings.

str_case = "where is the treasure located?"

print(str_case.upper())      # ALL UPPERCASE: WHERE IS THE TREASURE LOCATED?
print(str_case.lower())      # all lowercase: where is the treasure located?
print(str_case.capitalize()) # First char uppercase, rest lowercase: Where is the treasure located?
print(str_case.title())      # First Char Of Each Word Capitalized: Where Is The Treasure Located?
print(str_case.swapcase())   # Swap case of each character: WHERE IS THE TREASURE LOCATED?


# -----------------------------------------------------------------------------
# 5. STRING SEARCHING AND FINDING METHODS
# -----------------------------------------------------------------------------
# Methods to search for substrings within a string

search_str = "where is the treasure located?"

# Check if string starts with or ends with a specific substring
print(search_str.startswith('where'))    # Output: True
print(search_str.startswith('Where'))    # Output: False (case-sensitive!)
print(search_str.endswith('located?'))   # Output: True
print(search_str.endswith('treasure'))   # Output: False

# Find the starting index of a substring
# Returns -1 if substring is not found
treasure_index = search_str.find('treasure')
print(f'Index of "treasure": {treasure_index}')  # Output: Index of "treasure": 13

# Count occurrences of a substring
print(f'Letter "e" appears {search_str.count("e")} times')     # Output: Letter "e" appears 4 times
print(f'Word "the" appears {search_str.count("the")} times')   # Output: Word "the" appears 1 times


# -----------------------------------------------------------------------------
# 6. STRING VALIDATION METHODS
# -----------------------------------------------------------------------------
# Methods that check if a string matches certain criteria (return True or False)

validation_str = "where is the treasure located?"

# Check character types
print(validation_str.isalpha())   # False (contains spaces and punctuation)
print(validation_str.isdigit())   # False (contains letters)
print(validation_str.isspace())   # False (contains non-whitespace characters)

# Check case
print(validation_str.isupper())   # False (contains lowercase letters)
print(validation_str.islower())   # True (all letters are lowercase)

# Example with alphanumeric string
alpha_str = "Python3"
print(f'"{alpha_str}" is alphanumeric: {alpha_str.isalnum()}')  # True (letters + digits, no spaces)


# -----------------------------------------------------------------------------
# 7. OTHER USEFUL STRING METHODS
# -----------------------------------------------------------------------------

str_methods = "If I was a mushroom, life would be easier."

# Transform string content
print(str_methods.upper())   # IF I WAS A MUSHROOM, LIFE WOULD BE EASIER.
print(str_methods.lower())   # if i was a mushroom, life would be easier.

# Remove leading/trailing whitespace
str_with_spaces = "   hello world   "
print(str_with_spaces.strip())  # Output: hello world (no leading/trailing spaces)

# Replace substring with another
print(str_methods.replace('mushroom', 'scientist'))  # If I was a scientist, life would be easier.

# Split string into a list at specified delimiter
print(str_methods.split(','))  # Output: ['If I was a mushroom', ' life would be easier.']

# Join list elements into a single string with a separator
my_list = ['life', 'is', 'beautiful']
print('.'.join(my_list))  # Output: life.is.beautiful
print(' '.join(my_list))  # Output: life is beautiful


print("\n" + "="*60)
print("END OF SESSION 1")
print("="*60 + "\n")


