# =============================================================================
# LEARNING PYTHON - PART 2
# =============================================================================
# This is a continuation of learning_python.py
# Building upon the fundamentals covered in the initial file


# =============================================================================
# SESSION 3: 07/01/2026 — NUMERIC OPERATIONS AND OPERATORS
# =============================================================================
# This session covers numeric operations, arithmetic operators, type conversions,
# and augmented assignment operators in Python.

# -----------------------------------------------------------------------------
# 1. INTEGER ARITHMETIC OPERATIONS
# -----------------------------------------------------------------------------
# Python supports all basic arithmetic operations with integers.
# Integer division (/) always returns a float, even if the result is a whole number.

my_int = 4
my_int_2 = -3

print(type(my_int))    # <class 'int'>
print(type(my_int_2))  # <class 'int'>

# Basic arithmetic operations
print('Addition:', my_int + my_int_2)        # Output: 1
print('Subtraction:', my_int - my_int_2)     # Output: 7
print('Multiplication:', my_int * my_int_2)  # Output: -12
print('Division:', my_int / my_int_2)        # Output: -1.3333... (always returns float)


# -----------------------------------------------------------------------------
# 2. FLOAT ARITHMETIC OPERATIONS
# -----------------------------------------------------------------------------
# Floating-point numbers (floats) represent decimal values.
# All arithmetic operations work the same way as with integers.

my_float = 4.23
my_float_2 = -3.14

print(type(my_float))   # <class 'float'>
print(type(my_float_2)) # <class 'float'>

print('Addition:', my_float + my_float_2)        # Output: 1.09
print('Subtraction:', my_float - my_float_2)     # Output: 7.37
print('Multiplication:', my_float * my_float_2)  # Output: -13.2842
print('Division:', my_float / my_float_2)        # Output: -1.347133757


# -----------------------------------------------------------------------------
# 3. MIXED-TYPE ARITHMETIC (INT + FLOAT)
# -----------------------------------------------------------------------------
# When you perform operations between integers and floats,
# Python automatically converts the result to a float (type coercion).

sum_mixed = my_int + my_float
print(type(sum_mixed))      # <class 'float'> - result is automatically converted to float
print('Mixed Addition:', sum_mixed)  # Output: 8.23


# -----------------------------------------------------------------------------
# 4. ADVANCED ARITHMETIC OPERATORS
# -----------------------------------------------------------------------------
# Python provides additional operators for specialized calculations.

# MODULUS OPERATOR (%)
# Returns the remainder after division
print(my_float % my_float_2)  # Output: 1.09 - remainder of 4.23 / -3.14
print(my_int % my_int_2)      # Output: -2 - remainder of 4 / -3

# FLOOR DIVISION OPERATOR (//)
# Returns the largest integer less than or equal to the division result
print(7 // 3.8)  # Output: 1.0 - removes decimal part, keeps integer portion

# EXPONENTIATION OPERATOR (**)
# Raises a number to a power
print(my_float ** 2)  # Output: 17.8929 - 4.23 squared (4.23 × 4.23)


# -----------------------------------------------------------------------------
# 5. TYPE CONVERSION FUNCTIONS
# -----------------------------------------------------------------------------
# Python provides built-in functions to convert between numeric types.

# Converting strings to numbers
print(float('3.14'))  # Output: 3.14 - string to float
print(int('42'))      # Output: 42 - string to integer

# Converting floats to integers (truncates decimal part, doesn't round)
print(int(3.99))   # Output: 3 - simply removes decimal portion
print(int(-3.99))  # Output: -3 - truncates toward zero


# -----------------------------------------------------------------------------
# 6. ROUNDING AND ABSOLUTE VALUE
# -----------------------------------------------------------------------------

# ROUNDING
print(round(3.141))       # Output: 3 - rounds to nearest integer
print(round(3.147, 2))    # Output: 3.15 - rounds to 2 decimal places
print(round(2.5))         # Output: 2 - rounds to nearest even number (banker's rounding)
print(round(3.5))         # Output: 4

# ABSOLUTE VALUE
print(abs(-7.5))   # Output: 7.5 - distance from zero (always positive)
print(abs(7.5))    # Output: 7.5
print(abs(-10))    # Output: 10


# -----------------------------------------------------------------------------
# 7. POWER AND BASE CONVERSION FUNCTIONS
# -----------------------------------------------------------------------------

# THE pow() FUNCTION
# More versatile than the ** operator
print(pow(2, 3))        # Output: 8 - same as 2 ** 3 (2 to the power of 3)
print(pow(9, 0.5))      # Output: 3.0 - square root of 9 (9 ** 0.5)
print(pow(27, 1, 4))    # Output: 3 - modular exponentiation: (27 ** 1) % 4

# BASE CONVERSION WITH int()
# Converts strings in different bases to decimal integers
print(int('1010', 2))   # Output: 10 - binary (base-2) to decimal
print(int('FF', 16))    # Output: 255 - hexadecimal (base-16) to decimal
print(int('77', 8))     # Output: 63 - octal (base-8) to decimal
print(int('101', 10))   # Output: 101 - decimal (base-10, default)


# -----------------------------------------------------------------------------
# 8. AUGMENTED ASSIGNMENT OPERATORS
# -----------------------------------------------------------------------------
# Shorthand operators that combine an operation with assignment.
# Format: variable operator= value
# These make code more concise and readable.

# Numeric augmented assignments
my_var = 15
my_var += 5  # Equivalent to: my_var = my_var + 5
print('After += 5:', my_var)  # Output: 20

my_var -= 3  # Equivalent to: my_var = my_var - 3
print('After -= 3:', my_var)  # Output: 17

my_var *= 2  # Equivalent to: my_var = my_var * 2
print('After *= 2:', my_var)  # Output: 34

my_var //= 4  # Equivalent to: my_var = my_var // 4
print('After //= 4:', my_var)  # Output: 8

my_var %= 5  # Equivalent to: my_var = my_var % 5
print('After %= 5:', my_var)  # Output: 3

my_var **= 3  # Equivalent to: my_var = my_var ** 3
print('After **= 3:', my_var)  # Output: 27

# String augmented assignments
greet = "Hello"
greet += ", World!"  # Concatenates and assigns back
print(greet)  # Output: Hello, World!

greet *= 2  # Repeats the string twice
print(greet)  # Output: Hello, World!Hello, World!

# Note: Only += and *= work with strings
# Other operators (like -=, /=) will raise TypeError with strings

print("\n" + "="*60)
print("END OF SESSION 3")
print("="*60 + "\n")

# =============================================================================
# SESSION 4: 08/01/2026 — BOOLEANS AND CONDITIONALS
# =============================================================================
# This session covers comparison operators, conditional statements (if/elif/else),
# logical operators, and truthy/falsy values in Python.

# -----------------------------------------------------------------------------
# 1. COMPARISON OPERATORS
# -----------------------------------------------------------------------------
# Comparison operators compare two values and return a Boolean (True or False).
# They are essential for making conditional statements.

# List of comparison operators:
# ==  : Equal to (checks if two values are the same)
# !=  : Not equal to (checks if two values are different)
# >   : Greater than (left value is larger than right)
# <   : Less than (left value is smaller than right)
# >=  : Greater than or equal to
# <=  : Less than or equal to

# Examples of comparison operators
print(3 == 2)    # Output: False - 3 is not equal to 2
print(3 != 2)    # Output: True - 3 is different from 2
print(5 > 3)     # Output: True - 5 is greater than 3
print(2 < 10)    # Output: True - 2 is less than 10
print(5 >= 5)    # Output: True - 5 is equal to 5
print(3 <= 2)    # Output: False - 3 is not less than or equal to 2


# -----------------------------------------------------------------------------
# 2. THE if STATEMENT
# -----------------------------------------------------------------------------
# The if statement executes code only when a condition is True.
# Indentation (spaces/tabs) defines which code belongs to the if block.
# Python uses indentation instead of curly braces like other languages.

# Basic if statement structure:
# if condition:
#     code to execute if condition is True

age = 18
if age >= 18:
    print("You are an adult!")  # This prints because age >= 18 is True

# Using pass as a placeholder
# pass is a null operation - it does nothing but prevents syntax errors
if True:
    pass  # Placeholder for future code


# -----------------------------------------------------------------------------
# 3. THE if-else STATEMENT
# -----------------------------------------------------------------------------
# else provides an alternative block of code when the if condition is False.
# else never takes a condition - it's the "catch-all" for everything else.

age = 12
if age >= 18:
    print("You are an adult!")
else:
    print("You are not old enough yet!")  # Output: You are not old enough yet!

# Another example
temperature = 15
if temperature > 20:
    print("It's warm outside.")
else:
    print("It's cool outside.")  # This executes because 15 <= 20


# -----------------------------------------------------------------------------
# 4. THE elif STATEMENT (MULTIPLE CONDITIONS)
# -----------------------------------------------------------------------------
# elif (else if) allows you to check multiple conditions in sequence.
# Python evaluates conditions from top to bottom and executes the first True one.
# Once a condition is True, remaining elif/else blocks are skipped.

age = 16
if age < 13:
    print("You are a child.")
elif age < 18:
    print("You are a teenager.")  # This executes because 13 <= 16 < 18
elif age <= 25:
    print("You are a young adult.")
else:
    print("You are an adult.")

# Example with user input
# input() always returns a string, so we convert it to int
# Note: Commented out to allow script to run without interruption
# age = int(input("How old are you? "))
# if age < 13:
#     print("You are a child.")
# elif age < 18:
#     print("You are a teenager.")
# elif age <= 25:
#     print("You are a young adult.")
# else:
#     print("You are getting old, my friend.")


# -----------------------------------------------------------------------------
# 5. NESTED CONDITIONAL STATEMENTS
# -----------------------------------------------------------------------------
# You can place if statements inside other if statements (nesting).
# Each level of nesting adds another layer of indentation.
# Be careful with indentation - it determines which code belongs where!

# Note: Interactive examples commented out to allow script to run without interruption
# is_student = input("Are you a student? (yes/no): ")
# age = int(input("How old are you? "))
#
# if is_student == "yes":
#     print("You are eligible for a student discount!")
#     if age < 18:
#         print("You get an additional youth discount!")
#     else:
#         print("Standard student discount applies.")
# else:
#     print("No student discount available.")
#     if age < 18:
#         print("But you qualify for a youth discount!")
#     else:
#         print("Regular pricing applies.")

# Example with predefined values (demonstrates the same logic)
is_student = "yes"
age = 16

if is_student == "yes":
    print("You are eligible for a student discount!")
    if age < 18:
        print("You get an additional youth discount!")
    else:
        print("Standard student discount applies.")
else:
    print("No student discount available.")
    if age < 18:
        print("But you qualify for a youth discount!")
    else:
        print("Regular pricing applies.")


# -----------------------------------------------------------------------------
# 6. LOGICAL OPERATORS (and, or, not)
# -----------------------------------------------------------------------------
# Logical operators combine multiple conditions to create more complex logic.

# AND operator - ALL conditions must be True
age = 20
has_license = True
if age >= 18 and has_license:
    print("You can drive!")  # Both conditions are True, so this executes

# OR operator - AT LEAST ONE condition must be True
is_weekend = False
is_holiday = True
if is_weekend or is_holiday:
    print("No work today!")  # One condition is True, so this executes

# NOT operator - reverses the boolean value
is_raining = False
if not is_raining:
    print("You don't need an umbrella!")  # not False = True

# Another example with NOT
is_admin = True
if not is_admin:
    print("Access denied. Contact admin.")
else:
    print("Welcome, master!")  # This executes because is_admin is True

# Combining multiple logical operators
# Python evaluates: not first, then and, then or (can use parentheses for clarity)
age = 25
income = 50000
has_debt = False
if age >= 18 and income > 30000 and not has_debt:
    print("Loan approved!")  # All three conditions are True


# -----------------------------------------------------------------------------
# 7. TRUTHY AND FALSY VALUES
# -----------------------------------------------------------------------------
# In Python, every value has an inherent Boolean value (truthy or falsy).
# This means you can use any value in an if statement, not just True/False.

# TRUTHY VALUES (evaluate to True):
# - Non-zero numbers: 1, -5, 3.14, etc.
# - Non-empty strings: "hello", "a", etc.
# - Non-empty collections: [1, 2], {"key": "value"}, etc.

# FALSY VALUES (evaluate to False):
# - None
# - False (the boolean itself)
# - Integer 0
# - Float 0.0
# - Empty string ""
# - Empty list []
# - Empty tuple ()
# - Empty dictionary {}
# - Empty set set()

# Using bool() to check the Boolean value of any object
print(bool(0))           # Output: False - zero is falsy
print(bool(42))          # Output: True - non-zero number is truthy
print(bool(""))          # Output: False - empty string is falsy
print(bool("Hello"))     # Output: True - non-empty string is truthy
print(bool([]))          # Output: False - empty list is falsy
print(bool([1, 2, 3]))   # Output: True - non-empty list is truthy

# Practical examples using truthy/falsy values
# Note: Interactive examples commented out to allow script to run without interruption
# user_input = input("Enter your name (or press Enter to skip): ")
# if user_input:  # Non-empty string is truthy
#     print(f"Hello, {user_input}!")
# else:  # Empty string is falsy
#     print("Hello, anonymous!")

# Example with predefined value (demonstrates the same logic)
user_input = "Alice"
if user_input:  # Non-empty string is truthy
    print(f"Hello, {user_input}!")
else:  # Empty string is falsy
    print("Hello, anonymous!")

# Checking if a list has items
shopping_cart = []
if shopping_cart:
    print(f"You have {len(shopping_cart)} items in your cart.")
else:
    print("Your shopping cart is empty.")


print("\n" + "="*60)
print("END OF SESSION 4")
print("="*60 + "\n")


# =============================================================================
# SESSION 5: 09/01/2026 — FUNCTIONS AND BUILT-IN FUNCTIONS
# =============================================================================
# This session covers Python's built-in functions, how to define custom functions,
# function parameters, return values, and variable scope.

# -----------------------------------------------------------------------------
# 1. USING BUILT-IN FUNCTIONS
# -----------------------------------------------------------------------------
# Python comes with many pre-built functions that perform common tasks.
# You don't need to define them - they're always available.

# Note: Interactive examples commented out to allow script to run without interruption
# input() - Gets user input (always returns a string)
# name = input("What's your name? ")
# print("Hello, " + name + "!")
#
# mood = input("How are you feeling today? ")
# print("You are feeling", mood.lower(), "today.")
#
# int() - Converts a string to an integer
# age = int(input("How old are you? "))
# next_year_age = age + 1
# print("Next year, you will be", next_year_age, "years old.")
#
# len() - Returns the length of a string or collection
# favorite_color = input("What's your favorite color? ")
# color_length = len(favorite_color)
# print("Your favorite color has", color_length, "characters.")

# Example with predefined values (demonstrates the same logic)
name = "Alice"
print("Hello, " + name + "!")

mood = "Happy"
print("You are feeling", mood.lower(), "today.")

age = 25
next_year_age = age + 1
print("Next year, you will be", next_year_age, "years old.")

favorite_color = "blue"
color_length = len(favorite_color)
print("Your favorite color has", color_length, "characters.")


# -----------------------------------------------------------------------------
# 2. DEFINING YOUR OWN FUNCTIONS
# -----------------------------------------------------------------------------
# Functions are reusable blocks of code that perform specific tasks.
# Use the 'def' keyword to define a function.
# Syntax: def function_name(parameters):

def greet_user(username):
    """Greets the user by name."""
    # This is a docstring - it documents what the function does
    # Triple quotes allow multi-line documentation
    print("Hello, " + username.title() + "!")

# Calling the function with an argument
# Note: Interactive example commented out to allow script to run without interruption
# username = input("How do you want me to call you? ")
# greet_user(username)  # The value of username is passed to the function

# Example with predefined value (demonstrates the same logic)
username = "Bob"
greet_user(username)  # The value of username is passed to the function

# help() - Displays documentation (docstring) for a function
help(greet_user)  # Shows the docstring we wrote (also prints None as help() returns None)


# -----------------------------------------------------------------------------
# 3. PARAMETERS VS ARGUMENTS
# -----------------------------------------------------------------------------
# Parameters: Variables listed in the function definition (placeholders)
# Arguments: Actual values passed to the function when calling it

def calculate_sum(a, b):  # a and b are PARAMETERS
    """Returns the sum of two numbers."""
    return a + b

# When calling the function, we pass ARGUMENTS
result = calculate_sum(5, 3)  # 5 and 3 are ARGUMENTS
print("Sum:", result)  # Output: Sum: 8


# -----------------------------------------------------------------------------
# 4. RETURN STATEMENT VS PRINT
# -----------------------------------------------------------------------------
# return: Exits the function and sends a value back for later use
# print: Displays output to console but doesn't store it

def add_numbers(x, y):
    return x + y  # Returns the result - can be stored or used later

def display_sum(x, y):
    print(x + y)  # Just prints - result is lost after printing

# Using return
result = add_numbers(10, 5)  # result = 15 (stored in variable)
print("Result:", result)      # Can use the result later
double_result = result * 2    # Can perform more operations
print("Double:", double_result)

# Using print (no return value)
value = display_sum(10, 5)   # Prints 15, but value = None
print("Value:", value)        # Output: Value: None

# If you don't explicitly use return, Python returns None by default
def no_return():
    x = 10
    # No return statement

result = no_return()
print(result)  # Output: None


# -----------------------------------------------------------------------------
# 5. PRACTICAL FUNCTION EXAMPLE WITH USER INPUT
# -----------------------------------------------------------------------------

def calculate_sum_from_input(a, b):
    """Returns the sum of two numbers."""
    return a + b

# Note: Interactive example commented out to allow script to run without interruption
# Get input from user
# user_input = input("Enter two numbers separated by space: ")
# num1, num2 = user_input.split()  # split() divides string by spaces into a list
#
# # Convert strings to integers
# num1 = int(num1)
# num2 = int(num2)
#
# # Call function and display result
# result = calculate_sum_from_input(num1, num2)
# print("The sum is:", result)

# Example with predefined values (demonstrates the same logic)
user_input = "15 27"
num1, num2 = user_input.split()  # split() divides string by spaces into a list

# Convert strings to integers
num1 = int(num1)
num2 = int(num2)

# Call function and display result
result = calculate_sum_from_input(num1, num2)
print("The sum is:", result)


# -----------------------------------------------------------------------------
# 6. FUNCTION BEST PRACTICES
# -----------------------------------------------------------------------------
# 1. Use descriptive function names (verbs that describe the action)
# 2. Include docstrings to explain what the function does
# 3. Keep functions focused on a single task
# 4. Use return to make functions reusable
# 5. Choose clear parameter names

def calculate_area(width, height):
    """Calculates the area of a rectangle."""
    return width * height

# Good: descriptive name, clear purpose, returns a value
area = calculate_area(5, 10)
print(f"Area: {area} square units")


# --------------------------------------------------------------------------------
# 7. SCOPE OF VARIABLES
# --------------------------------------------------------------------------------
# Scope refers to the accessibility of variables in different parts of the code.
# Python follows the LEGB rule for variable scope:
# L - Local: Variables defined inside a function (accessible only within that function)
# E - Enclosing: Variables defined in enclosing or nested functions
# G - Global: Variables defined at the top level of a module or script (accessible anywhere)
# B - Built-in: Names pre-defined in Python (like print, len, etc.)

# Local Scope — variable declared inside a function or class can only be accessed within that function or class.
def my_func():
    local_var = "Hey, I'm local!"
    print(local_var)  

my_func()  # This works

# print(local_var)  # This would raise a NameError because local_var is not defined outside the function


# Enclosing Scope — function that's nested inside another function can access variables of the functions it's nested within.
def outer_func():
    out_msg = "Hello from the outer function!"

    def inner_func():
        # in_msg = 'How are you?' # If we define variable here, it would be local to inner_func, and not accessible outside.
        print(out_msg)  # Accessing variable from the enclosing function
    
    inner_func()
outer_func()  # This works

# Solution to access variable from inner function 
# Initialize in_msg in the outer function, then within inner function, make in_msg nonlocal to modify it.
def another_outer_func():
    out_msg = "Hello from another outer function!"
    in_msg = ""

    def another_inner_func():
        nonlocal in_msg  # Declare in_msg as nonlocal to modify it
        in_msg = 'How are you?'
        print(out_msg)  # Accessing variable from the enclosing function

    another_inner_func()
    print(in_msg)  # Now in_msg is accessible here because we declared it as nonlocal
another_outer_func()  # This works

# Global Scope — variables declared outside any function or class and can be accessed from anywhere in the script.
global_var = "I'm a global variable!"

def access_global():
    print(global_var)  # Accessing global variable
access_global()  # This works
print(global_var)  # This also works

# Using the global keyword to modify a global variable inside a function
global_var_2 = 11 # Global variable

def modify_global():
    global global_var_2 # Allows modification of the global variable
    global_var_2 += 9 # Modify the global variable

    global local_var_2 # Declare local_var_2 as global
    local_var_2 = "Local variable made global"
    print("Inside function, modified global_var_2:", global_var_2)
    print("Inside function, local_var_2:", local_var_2)

modify_global()  # This works
print("Outside function, global_var_2:", global_var_2)  # The change
print("Outside function, local_var_2:", local_var_2)  # This works because local_var_2 is global now

# Built-in Scope — names that are pre-defined in Python and can be accessed from anywhere
print(str(123))  # Using built-in str() function to convert integer to string
print(len("Hello"))  # Using built-in len() function to get length of string
print(max(5, 10, 3))  # Using built-in max() function to get the maximum value
# etc..


print("\n" + "="*60)
print("END OF SESSION 5")
print("="*60 + "\n")
