# Python Basics: Introductory Concepts and Code Examples

"""
Topics covered include:
1. Python syntax, variable assignment, and arithmetic operators.
2. Strings, conditionals, loops, and type conversions.
3. Built-in Python functions like `print`, `type`, `min`, `max`, `abs`, and more.
"""

# --- Hello, Python! ---

# Variable assignment: Define a variable `spam_amount` and initialize it to 0
spam_amount = 0
print(spam_amount)  # Output: 0

# Ordering Spam, egg, Spam, Spam, bacon, and Spam (add 4 servings of Spam)
spam_amount = spam_amount + 4

# Conditional statement: Check if Spam is ordered
if spam_amount > 0:
    print("But I don't want ANY spam!")

# String repetition: Create a "viking_song" with Spam repeated `spam_amount` times
viking_song = "Spam " * spam_amount
print(viking_song)  # Output: Spam Spam Spam Spam 

"""
Key Concepts:
1. Variables: No need to declare or specify types in Python.
2. Comments: Start with `#` and are ignored by Python.
3. Strings: Use double or single quotes. The `*` operator repeats strings.
4. Conditionals: Use `if` and indent blocks of code under it.
"""

# --- Numbers and Arithmetic in Python ---

# Examples of different number types
spam_amount = 0
print(type(spam_amount))  # Output: <class 'int'>

price = 19.95
print(type(price))  # Output: <class 'float'>

# Arithmetic operators
a, b = 5, 2
print(a + b)  # Addition: Output: 7
print(a - b)  # Subtraction: Output: 3
print(a * b)  # Multiplication: Output: 10
print(a / b)  # True division: Output: 2.5
print(a // b)  # Floor division: Output: 2
print(a % b)  # Modulus: Output: 1
print(a ** b)  # Exponentiation: Output: 25

# Example: Operator precedence (PEMDAS)
hat_height_cm = 25
my_height_cm = 190

# Incorrect order of operations
total_height_meters = hat_height_cm + my_height_cm / 100
print("Height in meters =", total_height_meters)  # Output: 26.9 (wrong)

# Correct order using parentheses
total_height_meters = (hat_height_cm + my_height_cm) / 100
print("Height in meters =", total_height_meters)  # Output: 2.15

# --- Built-in Functions for Numbers ---

# min and max functions
print(min(1, 2, 3))  # Output: 1
print(max(1, 2, 3))  # Output: 3

# abs function: Absolute value
print(abs(32))   # Output: 32
print(abs(-32))  # Output: 32

# Type conversion: int and float
print(float(10))   # Convert to float: Output: 10.0
print(int(3.33))   # Convert to int (truncates): Output: 3
print(int('807') + 1)  # Convert string to int: Output: 808

"""
Takeaways:
1. Python operators are versatile. For example, `*` multiplies numbers and repeats strings.
2. Built-in functions like `min`, `max`, `abs`, `int`, and `float` simplify operations.
3. Use parentheses to enforce the desired order of operations.
"""
