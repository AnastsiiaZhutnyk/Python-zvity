class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade


class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}, Grade: {self.grade}"


class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        return f"{self.name}: {self.sound}"


class Dog(Animal):
    def __init__(self, name, sound, breed):
        super().__init__(name, sound)
        self.breed = breed


class Bird:
    def fly(self):
        return None


class Sparrow(Bird):
    def fly(self):
        return "Sparrow flies high"


class Penguin(Bird):
    def fly(self):
        return "Penguin cannot fly"


class Encapsulation:
    def __init__(self, public, private, protected):
        self.public = public
        self._private = private
        self.__protected = protected


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


class AverageCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_average(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)


# Приклади виклику функцій з очікуваним виводом
# Student class
student1 = Student("Alice", 20, "A")
print(student1.display_info())  

# Animal and Dog classes
dog = Dog("Buddy", "Woof", "Golden Retriever")
print(dog.make_sound()) 
print(f"Breed: {dog.breed}") 

# Bird, Sparrow, and Penguin classes
sparrow = Sparrow()
penguin = Penguin()
print(sparrow.fly())  
print(penguin.fly())  

# Encapsulation class
encap = Encapsulation("Public Data", "Private Data", "Protected Data")
print(encap.public) 
print(encap._private)  
# print(encap.__protected)  # Це викличе AttributeError, тому що __protected є прихованим

# Rectangle class
rectangle = Rectangle(5, 10)
print(rectangle.calculate_perimeter()) 

# AverageCalculator class
calculator = AverageCalculator([10, 20, 30, 40, 50])
print(calculator.calculate_average())  

calculator_empty = AverageCalculator([])
print(calculator_empty.calculate_average())  