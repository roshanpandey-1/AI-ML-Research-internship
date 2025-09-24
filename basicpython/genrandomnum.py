#generating random numbers
import random

for i in range(10):
    print(random.randint(10, 20))


members = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
leader = random.choices(members, k=3)  # Randomly select 3 members from the list
print(leader)

class Dice:
    def roll(self):
        print(f'({random.randint(1, 6)},{random.randint(1,6)})')  # Simulating a dice roll

dice = Dice()
dice.roll()  # Roll the dice
