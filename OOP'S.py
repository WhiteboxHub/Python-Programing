'''
Write a class Person with private attributes name and age. Provide public methods to set and get these attributes.
'''

# class Person:
#     def __init__(self, name, age):
#         self.__name = name  # private attribute
#         self.__age = age    # private attribute

#     # Public method to set name
#     def set_name(self, name):
#         self.__name = name

#     # Public method to get name
#     def get_name(self):
#         return self.__name

#     # Public method to set age
#     def set_age(self, age):
#         self.__age = age

#     # Public method to get age
#     def get_age(self):
#         return self.__age

# # Test case
# person = Person("Alice", 30)
# print(person.get_name())  # Output: Alice
# print(person.get_age())   # Output: 30
# person.set_name("Bob")
# print(person.get_name())  # Output: Bob

'''
Write a base class Animal and a derived class Dog that inherits from Animal. The Dog class should have an additional method bark().
'''

# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound"

# class Dog(Animal):
#     def __init__(self, name, breed):
#         super().__init__(name)  # Call the constructor of the base class
#         self.breed = breed

#     def bark(self):
#         return f"{self.name} barks!"

# # Test case
# dog = Dog("Buddy", "Golden Retriever")
# print(dog.speak())   # Output: Buddy makes a sound (inherited method)
# print(dog.bark())    # Output: Buddy barks!


'''
Write a class Shape with a method area(). Then, create two subclasses Circle and Rectangle, both overriding the area() method.
'''

# class Shape:
#     def area(self):
#         return 0

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * (self.radius ** 2)

# class Rectangle(Shape):
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width

#     def area(self):
#         return self.length * self.width

# # Test case
# circle = Circle(5)
# print(circle.area())  # Output: 78.5 (Circle's area)

# rectangle = Rectangle(4, 5)
# print(rectangle.area())  # Output: 20 (Rectangle's area)


'''
Write an abstract class Vehicle with an abstract method move().
 Create two subclasses Car and Bike, both implementing the move() method.
'''

# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def move(self):
#         pass

# class Car(Vehicle):
#     def move(self):
#         return "Car is moving on the road"

# class Bike(Vehicle):
#     def move(self):
#         return "Bike is moving on the road"

# # Test case
# car = Car()
# print(car.move())  # Output: Car is moving on the road

# bike = Bike()
# print(bike.move())  # Output: Bike is moving on the road

'''
Write a class Rectangle with private attributes length and width.
 Use property decorators to define getter and setter methods for these attributes.
'''

# class Rectangle:
#     def __init__(self, length, width):
#         self.__length = length
#         self.__width = width

#     @property
#     def length(self):
#         return self.__length

#     @length.setter
#     def length(self, value):
#         if value > 0:
#             self.__length = value
#         else:
#             print("Length must be positive!")

#     @property
#     def width(self):
#         return self.__width

#     @width.setter
#     def width(self, value):
#         if value > 0:
#             self.__width = value
#         else:
#             print("Width must be positive!")

#     def area(self):
#         return self.__length * self.__width

# # Test case
# rect = Rectangle(4, 5)
# print(rect.area())  # Output: 20
# rect.length = 6
# print(rect.area())  # Output: 30
# rect.length = -3  # Output: Length must be positive!

'''
Write a class Person and another class Employee. 
Create a third class Manager that inherits from both Person and Employee.
'''

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         return f"Hello, {self.name}"

# class Employee:
#     def __init__(self, employee_id):
#         self.employee_id = employee_id

#     def work(self):
#         return f"Employee {self.employee_id} is working"

# class Manager(Person, Employee):
#     def __init__(self, name, employee_id):
#         Person.__init__(self, name)
#         Employee.__init__(self, employee_id)

#     def manage(self):
#         return f"Manager {self.name} is managing the team"

# # Test case
# manager = Manager("Alice", 101)
# print(manager.greet())  # Output: Hello, Alice
# print(manager.work())   # Output: Employee 101 is working
# print(manager.manage()) # Output: Manager Alice is managing the team


'''
Write a class MathOperations with a class method create_instance
 that returns a new instance of the class and a static method add() that returns the sum of two numbers.
'''
# class MathOperations:
#     def __init__(self, value):
#         self.value = value

#     @classmethod
#     def create_instance(cls, value):
#         return cls(value)

#     @staticmethod
#     def add(x, y):
#         return x + y

# # Test case
# math_obj = MathOperations.create_instance(10)
# print(math_obj.value)  # Output: 10

# result = MathOperations.add(5, 7)
# print(result)  # Output: 12


