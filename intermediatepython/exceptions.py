# exceptions.py

# ZeroDivisionError
try:
    x = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# Multiple exceptions
try:
    age = int(input("Enter your age: "))
    income = float(input("Enter your income: "))
    risk = income / age
    print(f"Your risk is {risk}.")
    print(f"You are {age} years old.")
except ZeroDivisionError:
    print("Age cannot be zero!")
except ValueError:
    print("Invalid input! Please enter valid numbers.")

# Catching generic Exception
try:
    a = [1, 2, 3]
    print(a[5])  # IndexError
except Exception as e:
    print("Error:", e)

# finally and else
try:
    num = int(input("Enter a number: "))
    result = 10 / num
except ZeroDivisionError:
    print("Cannot divide by zero.")
except ValueError:
    print("Please enter a valid number.")
else:
    print("Division successful:", result)
finally:
    print("This will always run (cleanup code).")

# raise (handled)
x = -5
try:
    if x < 0:
        raise ValueError("Negative value is not allowed")
except ValueError as e:
    print("Error:", e)

# ValueError
try:
    num = int("hello")  # invalid conversion
except ValueError:
    print("Invalid value for integer conversion.")

# TypeError
try:
    result = "5" + 2   # string + int not allowed
except TypeError:
    print("You cannot add string and integer.")

# IndexError
try:
    nums = [1, 2, 3]
    print(nums[5])  # index out of range
except IndexError:
    print("Index out of range.")

# KeyError
try:
    student = {"name": "Roshan"}
    print(student["age"])  # no such key
except KeyError:
    print("Key not found in dictionary.")

# FileNotFoundError
try:
    f = open("missing.txt", "r")
except FileNotFoundError:
    print("File does not exist.")

# AttributeError
try:
    x = 10
    x.append(5)   # int has no append
except AttributeError:
    print("Attribute not found for this object.")

# ImportError / ModuleNotFoundError (handled safely)
try:
    import not_a_real_module
except ModuleNotFoundError:
    print("Module not found.")

# Define risky_code so it doesn't break
def risky_code():
    return 10 / 0   # intentionally risky

# Catching all exceptions at once
try:
    risky_code()
except Exception as e:
    print("Error occurred:", e)


#custom exception
class NegativeNumberError(Exception):
    pass

def check_number(x):
    if x < 0:
        raise NegativeNumberError("Number cannot be negative")

try:
    check_number(-5)
except NegativeNumberError as e:
    print("Custom Error:", e)


#context manager with exception handling
try:
    with open("file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("File not found.")

# Using assertions
def divide(a, b):
    assert b != 0, "Denominator cannot be zero"
    return a / b

try:
    print(divide(10, 0))
except AssertionError as e:
    print("Assertion Error:", e)
    