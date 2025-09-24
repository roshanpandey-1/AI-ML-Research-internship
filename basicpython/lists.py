#lists
names =['ram', 'shyam', 'mohan', 'sita', 'gita']
print(names[0]) # ram
print(names[1]) # shyam   
print(names[0:4]) 


num =[1,4,9,20,2,5,8,19]
largest = num[0]
for i in num:
    if i > largest:
        largest = i
print(largest) # 20


#2d list

matrix = [[1,2,3],[4,5,6],[7,8,9]]  
print(matrix[0][0]) # 1
print(matrix[1][2]) # 6
for row in matrix:
    for col in row:
        print(col, end=" ")
    print() # 1 2 3 4 5 6 7 8 9 


#list methods
num =[1,4,9,20,2,5,8,19]
num.append(10) # add 10 to the end of the list
num.insert(0, 0) # add 0 to the beginning of the list
num.pop() # remove the last element of the list
print(num) # [0, 1, 4, 9, 20, 2, 5, 8, 19, 10]
print(num.index(20)) # 4
print(40 in num)
num.sort() # sort the list in ascending order
print(num)  


num =[1,2,4,9,20,2,5,8,19]
for i in num:
    count = 0
    for j in num:
        if i == j:
            count += 1
    if count > 1:
        num.remove(i)
        num.sort()
print(num) 

num = [1, 2, 4, 9, 20, 2, 5, 8, 19]
unique = []
for i in num:
    if i not in unique:
        unique.append(i)
unique.sort()
print(unique)


#tuples
num = (1, 2, 4, 9, 20, 2, 5, 8, 19)
print(num[0]) # 1
print(num[1]) # 2
print(num[0:4]) # (1, 2, 4, 9)
print(num.count(2)) # 2
print(num.index(20)) # 4
print(20 in num) # True    
print(40 in num) # False
print(len(num)) # 9



#unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates 
print(x) # 1
print(y) # 2    

