#while loops
i =1
while i <= 5:
    print('*' * i)
    i += 1
print ('Done')

#guess the number game
secret_number = 9
guess_count = 0
guess_limit = 3
guess_number = 0
while  guess_count < guess_limit:
    guess_number = int(input('Guess the number: '))
    guess_count += 1
    if guess_number == secret_number:
        print('You won!')
        break
else:
    print('You lose!')


#simple car game using while loop
print('''
start - to start the car
stop - to stop the car
quit - to exit
''')
started = False
stopped = False
while True:
    command = input('> ').lower()
    if command == 'start':
        if started:
            print('Car is already started')
        else:
            started = True
            print('Car started...')
    elif command == 'stop': 
        if stopped:
            print('Car is already stopped')
        else:
            stopped = True
            print('Car stopped...')
    elif command == 'quit':
        break
    else:
        print('wrong command')



#for loops
for item in 'python':
    print(item)

for item in ['python', 'java', 'c++']:
    print(item) 

for item in range(10):
    print(item)

prices = [10, 20, 30]
total = 0
for price in prices:
    total += price      
print('Total:', total)          


#nested loops
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

numbers = [2, 2, 2, 2, 6]
for x_count in numbers:
    for count in range(x_count):
        output = 'x' * x_count
    print(output)


