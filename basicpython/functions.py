def greet_user():
    print("Hello, welcome to the program!")
    
print("This is a module named functions.py")
greet_user()
print("This is a function in functions.py")

#parameters
def greet_user(name):
    print(f"Hello, {name}! Welcome to the program!")

greet_user("Alice")

#keyword arguments
def greet_user(name, age):
    print(f"Hello, {name}! You are {age} years old.")

greet_user(name="Bob", age=30)
greet_user(age=25, name="Charlie")        

#return statement
def add_numbers(a, b):
    return a + b    

print(f"The sum is: {add_numbers(5, 10)}")

def multiply_numbers(a, b):
    print(f"the multiplication of the number is: {a * b}")

multiply_numbers(5, 10)    

#creating areusable function
def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "😊",
        ":(": "😢",
        ":D": "😄",
        ":P": "😜",
        "<3": "❤️"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output.strip()    
    
message = input("Enter a message: ")
result = emoji_converter(message)
print(result)

