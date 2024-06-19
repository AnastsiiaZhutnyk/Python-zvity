Лабораторна робота №10: OOP in Python
___
Мета роботи:
Метою даної лабораторної роботи є закріплення основ об'єктно-орієнтованого програмування (ООП) у Python шляхом створення та використання класів. Виконуючи завдання цієї лабораторної роботи, я навчуся реалізовувати різні концепції ООП, такі як інкапсуляція, успадкування, та поліморфізм. Виконуючи ці завдання, я покращу свої навички роботи з класами та об'єктами у Python, що є основоположними для розвитку як програміста.
___
Опис завдання:
```Python
Task 1: Class Creation
Create a Python class named “Student” with the following attributes: - name -
age - grade
Example of class usage:
student = Student(name="Ivan", age=30, grade="2")
Task 2: Create Method
Add a method named display_info() to the Student class that prints the
student’s name, age, and grade in the format “Name: [name], Age: [age],
Grade: [grade]”.
Example of class usage:
student = Student(name="Ivan", age=30, grade="2")
print(student.display_info()) # Name: Ivan, Age: 30, Grade: 2
Task 3: Inheritance
Create two classes: Animal and Dog. Animal should have attributes name
and sound. Add a make_sound() method to Animal that returns the string
“[name]: [sound]”. Dog should inherit from Animal and have an additional
attribute breed.
Example of class usage:
animal = Animal(name="Lala", sound="Auuuuuuu", breed="Spitz")
print(animal.make_sound()) # Lala: 
print(dog.make_sound())  # Lala: Auuuuuu
Task 4: Polymorphism
Create a class Bird with a method fly() that returns None. Then create two
subclasses: Sparrow and Penguin. Override the fly() method in Sparrow
to return the string “Sparrow flies high” and in Penguin to return the string
“Penguin cannot fly”.
Example of class usage:
bird = Bird()
sparrow = Sparrow()
penguin = Penguin()
print(bird.fly()) # None
print(sparrow.fly()) # Sparrow flies high
print(penguin.fly()) # Penguin cannot fly
Task 5: Encapsulation
Create a class Encapsulation with the following attributes:
• public
• _private
• __protected
Example of class usage:
obj = Encapsulation(1, 2, 3)
print(obj.public) # 1
print(obj._private) # 2
print(obj._Encapsulation__protected) # 3
print(obj.__protected) # AttributeError
Task 6: Rectangle
Create a Rectangle class that has width and height attributes, and a
calculate_perimeter() method that returns the perimeter of the shape.
Example of class usage:
rectangle = Rectangle(width=5, height=4)
print(rectangle.calculate_perimeter()) # 18
Task 7: AverageCalculator
Create an AverageCalculator class that has a numbers attribute and takes a
list of integers. The class should have a calculate_average() method that
returns the arithmetic mean of the numbers in the list.
Example of class usage:
numbers = [5, 10, 15, 20]
avg_calculator = AverageCalculator(numbers)
print(avg_calculator.calculate_average()) # Expected output: 12.5
```
___
Виконання роботи:
```Python
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

```
___
Результати:
```Python
Name: Alice, Age: 20, Grade: A
Buddy: Woof
Breed: Golden Retriever
Sparrow flies high
Penguin cannot fly
Public Data
Private Data
30
30.0
0

```
___
Висновки:У результаті виконання цієї лабораторної роботи я значно поглибила свої знання та навички в області об'єктно-орієнтованого програмування (ООП) у Python. Зокрема, я опанувала основні концепції ООП, такі як створення класів, методів, успадкування, поліморфізм та інкапсуляція.Я отримала практичний досвід створення та використання класів, що допоможе мені у подальшому розвитку. Ці навички є фундаментальними для розробки складних програмних систем і дозволять мені ефективно працювати з об'єктно-орієнтованими принципами у реальних проектах.

___