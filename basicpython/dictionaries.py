#dictionaries
customers = {  
    "name": "John Doe",
    "age": 30,
    "is active": True,
}
print(customers["name"]) # John Doe
print(customers["age"]) # 30    

print(customers.get("name")) # John Doe
print(customers.get("month")) # None
print(customers.get("month", "Not found")) # Not found  


phone = input("phone: ")
digits_mapping = { 
    "1": "one",
    "2": "two",   
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",        
    "7": "seven",
    "8": "eight",  
    "9": "nine",
    "0": "zero",
    }
output = ""          
for ch in phone:
    output += digits_mapping.get(ch, "!") +' ' # ! is the default value if the key is not found
print(output)

#emoji converter
message = input(">")
words = message.split(" ")
emojis = {
    ":)": "😊",
    ":(": "😞",
    ":D": "😀",
    ":P": "😜",
    ";)": "😉",
}
output = ""
for word in words:
    output += emojis.get(word, word) + " " # if the word is not found in the dictionary, it will return the word itself
    print(output)




