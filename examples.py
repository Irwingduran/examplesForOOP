#creating a simple class in python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

dog = Animal("Charlie")
print(dog.speak())


#creating a subclass 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

class Dog(Animal):
    def speak(self):
        return f"{self.name} barks!"

dog = Dog("Charlie")
print(dog.speak())

#super() function
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} says hello!"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

dog = Dog("Charlie", "Bulldog")
print(dog.breed)


#@property
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value >= 0:
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

circle = Circle(5)
print(circle.radius)
circle.radius = 10
print(circle.radius)

#encapsulation
class MyClass:
    def __init__(self):
        self.public = "Public"
        self._protected = "Protected"
        self.__private = "Private"

obj = MyClass()
print(obj.public)
print(obj._protected)
print(obj.__private)  # This will raise an AttributeError

#polymorphism
from collections.abc import Iterable

def get_length(item):
    if isinstance(item, Iterable):
        return len(item)
    else:
        return "Not iterable"

print(get_length("Hello"))
print(get_length([1, 2, 3]))
print(get_length(123))

#Abstract
#from abc import ABC, abstractmethod

class AbstractAnimal(ABC):
    @abstractmethod
    def speak(self):
        pass

class Dog(AbstractAnimal):
    def speak(self):
        return "Boww Boww!"

# You can't instantiate an AbstractAnimal
# animal = AbstractAnimal()  # This will raise a TypeError

dog = Dog()
print(dog.speak())


#static methods
class MyClass:
    @classmethod
    def class_method(cls):
        return "Class method called"

    @staticmethod
    def static_method():
        return "Static method called"

print(MyClass.class_method())
print(MyClass.static_method())

#operator overloading
class Mango:
    def __init__(self,x):
        self.x = str(x)
    def __add__(self,y):
        return self.x + y.x
obj1 = Mango(7)
obj2 = Mango('mangoes')
print(obj1+obj2)

#special methods
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

p = Person("Bob", 30)
print(str(p))
print(repr(p))

#composition 
class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

s = Salary(15000, 5000)
e = Employee("Ashwin", s)
print(e.salary.pay


#multiple inheritance
class Parent1:
    def method1(self):
        return "Parent1's method called"

class Parent2:
    def method2(self):
        return "Parent2's method called"

class Child(Parent1, Parent2):
    pass

c = Child()
print(c.method1())
print(c.method2())

#decorators 
class MyClass:
    @staticmethod
    def method():
        return "Static method called"

    @classmethod
    def classmethod(cls):
        return "Class method called"

print(MyClass.method())
print(MyClass.classmethod())


#singleton class
class Singleton:
    _instance = None

    @staticmethod
    def getInstance():
        if Singleton._instance == None:
            Singleton()
        return Singleton._instance

    def __init__(self):
        if Singleton._instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton._instance = self

s = Singleton.getInstance()
print(s)

#mixin classes
class Mixin1(object):
    def test(self):
        print("Mixin1")

class Mixin2(object):
    def test(self):
        print("Mixin2")

class MyClass(Mixin1, Mixin2):
    pass

obj = MyClass()
obj.test()
