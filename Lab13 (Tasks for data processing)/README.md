Лабораторна робота №13: Tasks for data processing. Functions with different parameter types for solving data processing tasks.

___
Мета роботи:
Мета цієї лабораторної роботи полягає в ознайомленні з різноманітними аспектами програмування на Python, такими як робота зі списками, матрицями, генераторами, робота з рядками за допомогою регулярних виразів, сортування та обробка даних, включаючи групування, обробку великих обсягів даних в партіях та видалення викидів. Кожна з функцій, запропонованих у завданнях, надає можливість розвинути вміння управляти даними, ефективно використовувати вбудовані структури даних Python та вирішувати типові завдання, що можуть виникнути під час програмування.
___
Опис завдання:
```Python
Task 1: Interpolate Missing Values
Create a function interpolate_missing that takes a list of numbers, which may
include None as a placeholder for missing values. The function should interpolate
missing values using the average of the nearest non- None neighbors.
Example of function usage:print(interpolate_missing([1, None, None, 4])) # Output: [1, 2,
3, 4]
Task 2: Fibonacci Series Generator
Write a generator function fibonacci that yields the Fibonacci series up to n
terms.
Example of function usage:for num in fibonacci(5):
 print(num) # Output: 0, 1, 1, 2, 3
Task 3: Batch Data Processing
Define a function process_batches that takes a list of numbers and a batch size,
then processes each batch to return their maximum values.
Example of function usage:print(process_batches([1, 2, 3, 4, 5, 6], 2)) # Output: [2, 4,
6]
Task 4: Encode and Decode Strings
Create two functions encode_string and decode_string . encode_string
should convert the string into a run-length encoded format, and decode_string
should revert it back to the original string.
Example of function usage:encoded = encode_string("aaabbc")
print(encoded) # Output: "3a2bc"
print(decode_string(encoded)) # Output: "aaabbc"
Task 5: Matrix Rotation
Write a function rotate_matrix that rotates a given n x n matrix 90 degrees
clockwise.
Example of function usage:matrix = [
 [1, 2],
 [3, 4]
]
print(rotate_matrix(matrix)) # Output: [[3, 1], [4, 2]]
Task 6: Regular Expression Search
Define a function regex_search that takes a list of strings and a regular
expression pattern, returning a list of all strings that match the pattern.
Example of function usage:print(regex_search(["test", "test123", "none"], "test\d+")) #
Output: ["test123"]
Task 7: Merge Sorted Arrays
Create a function merge_sorted_arrays that merges two sorted arrays into a
single sorted array.
Example of function usage:print(merge_sorted_arrays([1, 3, 5], [2, 4, 6])) # Output: [1,
2, 3, 4, 5, 6]
Task 8: Prime Number Checker
Write a function is_prime that takes a number and returns True if it is a prime
number, otherwise False .
Example of function usage:print(is_prime(11)) # Output: True
Task 9: Group by Key
Define a function group_by_key that takes a list of dictionaries and groups them
by a specified key.
Example of function usage:data = [{'key': 'a', 'value': 1}, {'key': 'b', 'value': 2},
{'key': 'a', 'value': 3}]
print(group_by_key(data, 'key')) # Output: {'a': [1, 3], 'b':
[2]}
Task 10: Remove Outliers
Create a function remove_outliers that removes elements from a list that are
more than two standard deviations away from the mean.
Example of function usage:print(remove_outliers([10, 100, 200, 300, 400, 500, 600])) #
Output: [100, 200, 300, 400, 500]


```
___
Виконання роботи:
```Python
def interpolate_missing(nums):
    interpolated = []
    for i, num in enumerate(nums):
        if num is None:
            left_index = i - 1
            right_index = i + 1
            left_value = None
            right_value = None
            while left_index >= 0:
                if nums[left_index] is not None:
                    left_value = nums[left_index]
                    break
                left_index -= 1
            while right_index < len(nums):
                if nums[right_index] is not None:
                    right_value = nums[right_index]
                    break
                right_index += 1

            if left_value is not None and right_value is not None:
                distance = right_index - left_index
                interpolated_value = left_value + ((right_value - left_value) / distance) * (i - left_index)
                interpolated.append(round(interpolated_value))
            elif left_value is not None:
                interpolated.append(left_value)
            elif right_value is not None:
                interpolated.append(right_value)
            else:
                interpolated.append(None)
        else:
            interpolated.append(num)
    return interpolated


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def process_batches(nums, batch_size):
    return [max(nums[i:i + batch_size]) for i in range(0, len(nums), batch_size)]


def encode_string(s):
    encoded = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded += str(count) + s[i - 1]
            count = 1
    encoded += str(count) + s[-1]
    return encoded
def encode_string(s):
    enco= ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count > 1:
                enco += str(count)
            enco += s[i - 1]
            count = 1
    if count > 1:
        enco += str(count)
    enco += s[-1]
    return enco
def decode_string(s):
    dec = ''
    i = 0
    while i < len(s):
        if s[i].isdigit():
            count = int(s[i])
            dec += s[i + 1] * count
            i += 2
        else:
            dec += s[i]
            i += 1
    return dec


def rotate_matrix(matrix):
    return [list(row) for row in zip(*matrix[::-1])]


import re


def regex_search(strings, pattern):
    return [string for string in strings if re.search(pattern, string)]


def merge_sorted_arrays(arr1, arr2):
    merged = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def group_by_key(data, key):
    grouped = {}
    for item in data:
        grouped.setdefault(item[key], []).append(item['value'])
    return grouped


import numpy as np


def remove_outliers(lst):
    mean = np.mean(lst)
    std_dev = np.std(lst)
    z_scores = [(x - mean) / std_dev for x in lst]
    threshold = 2

    return [x for x, z in zip(lst, z_scores) if abs(z) <= threshold]


# Приклади виклику функцій з очікуваним виводом
nums = [None, 2, None, 8, None, 12, None]
print(interpolate_missing(nums))  

fib_gen = fibonacci(10)
print(list(fib_gen))  

nums = [3, 10, 5, 8, 2, 7, 1, 9]
batch_size = 3
print(process_batches(nums, batch_size))

s = "aaabbcddd"
print(encode_string(s))  

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(rotate_matrix(matrix))  

strings = ["apple", "banana", "orange", "grape"]
pattern = r"an"
print(regex_search(strings, pattern))  
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sorted_arrays(arr1, arr2)) 

num = 17
print(is_prime(num)) 

data = [
    {"key": "A", "value": 1},
    {"key": "B", "value": 2},
    {"key": "A", "value": 3},
    {"key": "B", "value": 4}
]
print(group_by_key(data, "key"))  

lst = [1, 2, 3, 100, 5, 6, 200, 8, 9]
print(remove_outliers(lst))  


```
___
Результати:
```Python
[2, 2, 5, 8, 10, 12, 12]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
[10, 8, 9]
"3a2b1c3d"
[[7, 4, 1], [8, 5, 2], [9, 6, 3]]
["banana", "orange"]
[1, 2, 3, 4, 5, 6]
True
{'A': [1, 3], 'B': [2, 4]}
[1, 2, 3, 5, 6, 8, 9]

```
___
Висновки:Ця лабораторна робота дозволила мені краще розібратися з базовими конструкціями Python, включаючи цикли, умовні оператори, списки, рядки, функції, класи та методи. Кожне завдання створює можливість для практичного використання цих концепцій у реальних сценаріях, що є корисним для набуття досвіду у програмуванні. Такий підхід сприяє збагаченню загального розуміння мови Python та підготовці до більш складних завдань.