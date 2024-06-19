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
