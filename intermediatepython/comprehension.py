# List comprehension
numbers1 = [1, 2, 3, 4, 5, 6]
squares = [n**2 for n in numbers1]
evens = [n for n in numbers1 if n % 2 == 0]
print(squares)  
print(evens)    

# Set comprehension
numbers2 = [1, 2, 2, 3, 4, 4, 5]
unique_squares = {n**2 for n in numbers2}
print(unique_squares)

# Dictionary comprehension
numbers3 = [1, 2, 3, 4, 5]
squared_dict = {n: n**2 for n in numbers3}
print(squared_dict)


# Generator expression
numbers4 = [1, 2, 3, 4, 5]
squared_gen = (n**2 for n in numbers4)
print(squared_gen)
print(next(squared_gen))  
print(next(squared_gen))
print(list(squared_gen))

# Nested list comprehension
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)

# Multiplication table using nested list comprehension
table = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(table)  

#nested set comprehension
matrix = [[1, 2, 2], [2, 3, 4], [4, 5, 6]]
unique_nums = {num for row in matrix for num in row}
print(unique_nums) 

#nested dictionary comprehension
matrix = [[1, 2], [3, 4]]
squared_dict = {i: {j: j**2 for j in row} for i, row in enumerate(matrix)}
print(squared_dict) 

product_dict = {(i, j): i * j for i in range(1, 4) for j in range(1, 4)}
print(product_dict)

#nested generator expression
gen = (num for row in [[1, 2], [3, 4]] for num in row)
print(list(gen))  


gen = ((i, j, i * j) for i in range(1, 4) for j in range(1, 4))
print(list(gen))  
for item in gen:
    print(item)
