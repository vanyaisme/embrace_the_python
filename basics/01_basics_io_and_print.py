# =============================================================================
# BASIC INPUT/OUTPUT AND PRINT OPERATIONS
# =============================================================================
# This module covers the fundamental I/O operations in Python:
# - Basic output with print()
# - Advanced print() features and parameters
# - Formatting output for better readability


# -----------------------------------------------------------------------------
# 1. BASIC OUTPUT WITH print()
# -----------------------------------------------------------------------------
# The print() function displays output to the console/terminal.
# It's one of the most fundamental functions in Python.

print("Hello World!")  # Output: Hello World!


# -----------------------------------------------------------------------------
# 2. ADVANCED print() FEATURES
# -----------------------------------------------------------------------------
# The print() function accepts multiple arguments and various parameters.

# Using the sep parameter to customize the separator between items
# Default separator is a space (' '), but you can change it to any string
print('My favorite drinks are', 'red bull', 'Fritz Cola', 'and', 'coffee.', sep=' > ')
# Output: My favorite drinks are > red bull > Fritz Cola > and > coffee.


print("\n" + "="*60)
print("END OF BASIC I/O MODULE")
print("="*60 + "\n")
