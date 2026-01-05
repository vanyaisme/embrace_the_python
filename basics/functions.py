"""
Functions in Python
===================
This module covers the basics of Python functions.
Learning topics:
- Function definition with def
- Function parameters
- Function calls
- Docstrings for documentation
"""

# =============================================================================
# BASIC FUNCTION EXAMPLE
# =============================================================================

print("Hello World!")  # This is a simple Python program that prints "Hello World!" to the console.


# =============================================================================
# FUNCTION WITH PARAMETERS
# =============================================================================

def greet(name):
    """
    Function to greet a person by their name.
    
    Args:
        name (str): The name of the person to greet
    """
    print(f'Hello, {name}!')


# Calling the function with the name "Alice"
greet("Alice")

print("End of functions.py")
