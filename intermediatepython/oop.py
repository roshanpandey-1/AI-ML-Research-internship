class MyClass:
  x = 5

p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p2 = Person("John", 36)

print(p2.name)
print(p2.age)

class Car:
    def __init__(self, brand, model):  # constructor
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"{self.brand} {self.model} is driving...")

car1 = Car("Tesla", "Model S")
car2 = Car("Toyota", "Corolla")

car1.drive()   
car2.drive()


#encapsulation
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance   

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

account = BankAccount(1000)
account.deposit(500)
print(account.get_balance())   


#abstraction
from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Bike started with kick")

bike = Bike()
bike.start()

#inheritance
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):   # inherits Animal
    def speak(self):
        print("Dog barks")

dog = Dog()
dog.speak()   # Dog barks


#polymorphism
# method overriding
class Bird:
    def fly(self):
        print("Some birds can fly")

class Sparrow(Bird):
    def fly(self):
        print("Sparrow flies high")

sparrow = Sparrow()
sparrow.fly()   

#operator overloading
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    def __add__(self, other):  
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(2, 3)
p2 = Point(4, 5)
p3 = p1 + p2
print(p3.x, p3.y)   

#special methods
class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"Book: {self.title}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

book = Book("Python Guide", 350)
print(book)        
print(len(book))   


#advanced concepts
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        if r > 0:
            self._radius = r
        else:
            raise ValueError("Radius must be positive")

c = Circle(5)
print(c.radius)  
c.radius = 10
print(c.radius)

