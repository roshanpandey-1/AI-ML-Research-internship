#exceptions
try:
    age = int(input("Enter your age: "))
    income = float(input("Enter your income: "))
    risk = income / age
    print(f"Your risk is {risk}.")
    print(f"You are {age} years old.")
except ZeroDivisionError:
    print("Age cannot be zero!")    
except ValueError:
    print("Invalid input! Please enter a valid number for age.")
