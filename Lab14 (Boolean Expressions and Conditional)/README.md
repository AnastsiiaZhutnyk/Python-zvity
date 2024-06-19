Лабораторна робота №14:Boolean Expressions and Conditional Statements
___
Мета роботи:
Мета даної лабораторної роботи полягає в розробці набору функцій на Python для виконання базових операцій з булевими значеннями та умовами. Кожна функція спрямована на вирішення конкретного завдання з області логіки програмування, таких як перевірка умов, логічні операції, обробка умовних виразів та фільтрація даних. Це дозволяє набути практичного досвіду у розробці функцій, що обробляють булеві значення, та оволодіти базовими концепціями програмування з використанням умовних конструкцій.
___
Опис завдання:
```Python
Task 1: Basic Boolean Operations
Write a function check_truth that takes three boolean parameters ( a , b , c )
and returns the result of the expression (a and b) or c .
Example of function usage:print(check_truth(True, False, True)) # True
Task 2: Logical Equivalence
Write a function logical_equivalence that takes two boolean parameters and
returns True if they are logically equivalent, otherwise False .
Example of function usage:print(logical_equivalence(True, True)) # True
print(logical_equivalence(True, False)) # False
Task 3: Exclusive Or (XOR)
Write a function xor that takes two boolean arguments and returns True if
exactly one of the arguments is True .
Example of function usage:print(xor(True, False)) # True
print(xor(True, True)) # False
Task 4: Conditional Greeting
Write a function greet that takes a boolean value. If True , the function should
return "Hello, World!", otherwise it should return "Goodbye, World!".
Example of function usage:print(greet(True)) # Hello, World!
print(greet(False)) # Goodbye, World!
Task 5: Nested Conditions
Write a function nested_condition that takes three integers ( x , y , z ). The
function should return "All same" if all three are equal, "All different" if they are all
different, and "Neither" otherwise.
Example of function usage:print(nested_condition(3, 3, 3)) # All same
print(nested_condition(3, 4, 5)) # All different
Task 6: Conditional Counting
Write a function count_true that accepts a list of boolean values and returns the
count of how many are True .
Example of function usage:print(count_true([True, False, True, False, True])) # 3
Task 7: Boolean Parity
Write a function parity that accepts an integer and returns True if the number
of 1 s in the binary representation of the number is even, otherwise False .
Example of function usage:print(parity(3)) # False (binary 11)
Task 8: Majority Vote
Write a function majority_vote that takes three boolean inputs and returns
True if more than half of them are True , otherwise False .
Example of function usage:print(majority_vote(True, True, False)) # True
Task 9: Boolean Switch
Write a function switch that takes a boolean value and returns its opposite.
Example of function usage:print(switch(True)) # False
Task 10: Ternary Operator Simulation
Write a function ternary_check that simulates a ternary operator. It takes three
parameters: a boolean condition, a result if true, and a result if false. It returns the corresponding result based on the condition.
Example of function usage:print(ternary_check(True, "Yes", "No")) # Yes
Task 11: Validate Combination
Write a function validate that takes three booleans ( x , y , z ) and returns
True if x is True or both y and z are True , otherwise False .
Example of function usage:print(validate(True, False, True)) # True
Task 12: Condition Chain
Write a function chain_check that evaluates a sequence of conditions. It takes
three integers and returns "Increasing" if they are in strictly increasing order,
"Decreasing" if in strictly decreasing order, or "Neither" otherwise.
Example of function usage:print(chain_check(1, 2, 3)) # Increasing
print(chain_check(3, 2, 1)) # Decreasing
Task 13: Boolean Filter
Write a function filter_true that takes a list of boolean values and returns a
new list containing only the True values.
Example of function usage:print(filter_true([True, False, True, False])) # [True, True]
Task 14: Conditional Multiplexer
Write a function multiplexer that takes four parameters: three boolean inputs
and one integer. If the first boolean is True , return double the integer. If the
second is True , return triple the integer. If the third is True , return the integer
minus five. If none are True , return the integer unchanged.
Example of function usage:print(multiplexer(False, False, True, 10)) # 5

```
___
Виконання роботи:
```Python
def check_truth(a, b, c):
    return (a and b) or c

def logical_equivalence(a, b):
    return a == b

def xor(a, b):
    return (a and not b) or (not a and b)

def greet(is_hello):
    if is_hello:
        return "Hello, World!"
    else:
        return "Goodbye, World!"

def nested_condition(x, y, z):
    if x == y == z:
        return "All same"
    elif x != y and y != z and x != z:
        return "All different"
    else:
        return "Neither"

def count_true(bool_list):
    count = 0
    for item in bool_list:
        if item:
            count += 1
    return count


def parity(number):
    binary_representation = bin(number)[2:]
    count_ones = binary_representation.count('1')

    return count_ones % 2 == 0

def majority_vote(a, b, c):
    count_true = sum([a, b, c])
    return count_true > 1

def switch(boolean_value):
    return not boolean_value

def ternary_check(condition, result_true, result_false):
    return result_true if condition else result_false

def validate(x, y, z):
    return x or (y and z)

def chain_check(a, b, c):
    if a < b < c:
        return "Increasing"
    elif a > b > c:
        return "Decreasing"
    else:
        return "Neither"

def filter_true(bool_list):
    return [value for value in bool_list if value]

def multiplexer(bool1, bool2, bool3, integer):
    if bool1:
        return integer * 2
    elif bool2:
        return integer * 3
    elif bool3:
        return integer - 5
    else:
        return integer



# Приклади виклику функцій з очікуваним виводом
print(check_truth(True, True, False))  

print(logical_equivalence(True, True))  
print(logical_equivalence(True, False))  

print(xor(True, True)) 
print(xor(True, False))  
print(greet(True)) 
print(greet(False))  

print(nested_condition(1, 1, 1)) 
print(nested_condition(1, 2, 3))  
print(nested_condition(1, 1, 2))  

print(count_true([True, False, True, True]))  

print(parity(5))  
print(parity(4))  

print(majority_vote(True, False, True))  
print(majority_vote(False, False, True))  

print(switch(True))  

print(ternary_check(True, "Yes", "No")) 
print(ternary_check(False, "Yes", "No")) 

print(validate(True, False, True))  
print(validate(False, True, True))  
print(validate(False, False, False)) 

print(chain_check(1, 2, 3))  
print(chain_check(3, 2, 1))  
print(chain_check(1, 2, 2))  

print(filter_true([True, False, True, False]))  

print(multiplexer(True, False, False, 10))  
print(multiplexer(False, True, False, 10))  
print(multiplexer(False, False, True, 10)) 
print(multiplexer(False, False, False, 10))  


```
___
Результати:
```Python
True
True
False
False
True
Hello, World!
Goodbye, World!
All same
All different
Neither
3
True
False
True
False
False
Yes
No
True
True
False
Increasing
Decreasing
Neither
[True, True]
20
30
5
10


```
___
Висновки:Ця лабораторна робота дозволила мені поглибити розуміння базових концепцій програмування та розвинути навички у написанні функцій для рішення різноманітних завдань на основі булевих операцій та умовних конструкцій.