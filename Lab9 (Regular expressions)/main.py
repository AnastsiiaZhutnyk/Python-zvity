import re


def task1(input_str):
    pattern = r'^[a-z0-9]+$'
    return bool(re.match(pattern, input_str))



def task2(input_str):
    pattern = r'[A-Z]'
    return bool(re.search(pattern, input_str))



def task3(input_str):
    pattern = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    return bool(re.match(pattern, input_str))



def task4(input_str):
    pattern = r'^([01]?[0-9]|2[0-3]):([0-5][0-9]):([0-5][0-9])$'
    return bool(re.match(pattern, input_str))



def task5(input_str):
    pattern = r'^\d{5}(-\d{4})?$'
    return bool(re.match(pattern, input_str))



def task6(input_str):
    pattern = r'^[a-z0-9_-]{6,12}$'
    return bool(re.match(pattern, input_str))



def task7(input_str):
    pattern = r'^[4-6]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
    return bool(re.match(pattern, input_str.replace("-", "")))



def task8(input_str):
    pattern = r'^\d{3}-\d{2}-\d{4}$'
    return bool(re.match(pattern, input_str))



def task9(input_str):
    pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%])[A-Za-z\d@#$%]{8,}$'
    return bool(re.match(pattern, input_str))



def task10(input_str):
    pattern = r'^([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$'
    return bool(re.match(pattern, input_str))

# Приклади виклику функцій з очікуваним виводом
print(task1("abc123")) 
print(task2("Abc"))     
print(task3("192.168.1.1"))  
print(task4("23:59:59"))   
print(task5("12345-6789"))  
print(task6("username1"))   
print(task7("4123-4567-8901-2345")) 
print(task8("123-45-6789"))   
print(task9("Password@123")) 
print(task10("2001:0db8:85a3:0000:0000:8a2e:0370:7334"))  