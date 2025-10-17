f = open("test.txt", "w") 
f.write("Hello, Python!\n")
f.close()


f = open("test.txt", "r")
print(f.read())   
f.close()


f = open("test.txt", "r")
print(f.read(5))   
f.close()

f = open("test.txt", "r")
print(f.readline())   
print(f.readline())  
f.close()

f = open("test.txt", "r")
lines = f.readlines()
print(lines)   
f.close()


# f = open("test.txt", "w")
# f.write("Overwritten text!")
# f.close()

f = open("test.txt", "a")
f.write("\nNew line added.")
f.close()


with open("test.txt", "r") as f:
    content = f.read()
    print(content)

with open("test.txt", "r") as f:
    print(f.read(5))   
    print(f.tell())    
    f.seek(0)          
    print(f.read(5))   

import os

# Check if file exists
if os.path.exists("test.txt"):
    print("File exists")

# Delete file
os.remove("test.txt")

#working with csv and json files

import csv

# Writing CSV
with open("data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age"])
    writer.writerow(["Alice", 25])
    writer.writerow(["Bob", 30])

# Reading CSV
with open("data.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)


import json

# Writing JSON
data = {"name": "Alice", "age": 25}
with open("data.json", "w") as f:
    json.dump(data, f)

# Reading JSON
with open("data.json", "r") as f:
    obj = json.load(f)
    print(obj)


#exception handling with files
try:
    with open("unknown.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("File not found!")

