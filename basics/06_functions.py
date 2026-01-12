# =============================================================================
# FUNCTIONS AND SCOPE
# =============================================================================
# This module covers function definitions, parameters, return values, and variable scope:
# - Basic function definition and calling
# - Using Python's built-in functions
# - Defining custom functions with docstrings
# - Parameters vs arguments
# - Return statement vs print
# - Practical function examples with user input
# - Function best practices
# - Variable scope (LEGB rule: Local, Enclosing, Global, Built-in)


# -----------------------------------------------------------------------------
# 1. BASIC FUNCTION DEFINITION AND CALLING
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
# 2. USING BUILT-IN FUNCTIONS
# -----------------------------------------------------------------------------
# Python comes with many pre-built functions that perform common tasks.
# You don't need to define them - they're always available.

# input() - Gets user input (always returns a string)
name = input("What's your name? ")
print("Hello, " + name + "!")

mood = input("How are you feeling today? ")
print("You are feeling", mood.lower(), "today.")

# int() - Converts a string to an integer
age = int(input("How old are you? "))
next_year_age = age + 1
print("Next year, you will be", next_year_age, "years old.")

# len() - Returns the length of a string or collection
favorite_color = input("What's your favorite color? ")
color_length = len(favorite_color)
print("Your favorite color has", color_length, "characters.")


# -----------------------------------------------------------------------------
# 3. DEFINING YOUR OWN FUNCTIONS WITH DOCSTRINGS
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
username = input("How do you want me to call you? ")
greet_user(username)  # The value of username is passed to the function

# help() - Displays documentation (docstring) for a function
help(greet_user)  # Shows the docstring we wrote


# -----------------------------------------------------------------------------
# 4. PARAMETERS VS ARGUMENTS
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
# 5. RETURN STATEMENT VS PRINT
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
# 6. PRACTICAL FUNCTION EXAMPLE WITH USER INPUT
# -----------------------------------------------------------------------------

def calculate_sum_from_input(a, b):
    """Returns the sum of two numbers."""
    return a + b


# Get input from user
user_input = input("Enter two numbers separated by space: ")
num1, num2 = user_input.split()  # split() divides string by spaces into a list

# Convert strings to integers
num1 = int(num1)
num2 = int(num2)

# Call function and display result
result = calculate_sum_from_input(num1, num2)
print("The sum is:", result)


# -----------------------------------------------------------------------------
# 7. FUNCTION BEST PRACTICES
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


# -----------------------------------------------------------------------------
# 8. SCOPE OF VARIABLES
# -----------------------------------------------------------------------------
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
global_var_2 = 11  # Global variable


def modify_global():
    global global_var_2  # Allows modification of the global variable
    global_var_2 += 9  # Modify the global variable

    global local_var_2  # Declare local_var_2 as global
    local_var_2 = "Local variable made global"
    print("Inside function, modified global_var_2:", global_var_2)
    print("Inside function, local_var_2:", local_var_2)


modify_global()  # This works
print("Outside function, global_var_2:", global_var_2)  # The change
# This works because local_var_2 is global now
print("Outside function, local_var_2:", local_var_2)

# Built-in Scope — names that are pre-defined in Python and can be accessed from anywhere
print(str(123))  # Using built-in str() function to convert integer to string
print(len("Hello"))  # Using built-in len() function to get length of string
print(max(5, 10, 3))  # Using built-in max() function to get the maximum value
# etc..


print("\n" + "="*60)
print("END OF FUNCTIONS AND SCOPE MODULE")
print("="*60 + "\n")
