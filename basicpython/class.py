#introduction to classes
class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")   
        

point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
print(point1.y)
point1.draw()
point1.move()

#constructors
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")

point1 = Point(10, 20)
print(point1.x)        

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello, my name is {self.name}")

person1 = Person("John")
person1.talk()      


#inheritance
class Animal:
    def walk(self):
        print("walk")

class Dog(Animal):
    def bark(self):
        print("bark")   
   
class Cat(Animal):
    def sound(self):
        print("meow")         

dog1 = Dog()
dog1.walk()
dog1.bark()
cat1 = Cat()
cat1.walk()
cat1.sound()

