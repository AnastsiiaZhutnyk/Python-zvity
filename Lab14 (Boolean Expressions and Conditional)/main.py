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