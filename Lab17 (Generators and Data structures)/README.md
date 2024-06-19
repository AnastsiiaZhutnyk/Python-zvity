Лабораторна робота №17: Generators and Data structures
___
Мета роботи:
Метою даної лабораторної роботи є практичне засвоєння та застосування концепцій генераторів у мові програмування Python. Також під час виконання роботи отримуєш знання створювати генератори для різних типів даних та структур, включаючи ітерацію списків, числові послідовності, роботу з файлами, словниками та деревами. Через реалізацію різноманітних завдань кожен зрозуміє, як генератори допомагають зменшити використання пам'яті та покращити продуктивність коду. 


Опис завдання:
```Python
Task 1: Create a generator to iterate over a list of numbers.
Create a generator function named number_generator that takes a list of numbers and yields each number one by one.
Example of function usage:
Task 2: Develop a generator that yields even numbers from a given range.
Create a generator function named even_number_generator that takes two integers, start and end , and yields even numbers within that range.
Example of function usage:
Task 3: Implement a generator to yield odd numbers within a specified range.
Create a generator function named odd_number_generator that takes two integers, start and end , and yields odd numbers within that range.
Example of function usage:
gen = number_generator([1, 2, 3, 4, 5])
print(next(gen))  # 1
print(next(gen))  # 2
gen = even_number_generator(1, 10)
print(next(gen))  # 2
print(next(gen))  # 4
gen = odd_number_generator(1, 10)
print(next(gen))  # 1
print(next(gen))  # 3
Task 4: Write a generator that produces Fibonacci numbers.
Create a generator function named fibonacci_generator that produces Fibonacci numbers indefinitely.
Example of function usage:
  gen = fibonacci_generator()
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 1
print(next(gen))  # 2
Task 5: Create a generator that yields prime numbers up to a given limit.
Create a generator function named prime_number_generator that takes an integer limit and yields prime numbers up to that limit.
Example of function usage:
Task 6: Develop a generator to traverse a binary tree in pre-order.
Create a generator function named pre_order_traversal that takes the root of a binary tree and yields its nodes in pre-order.
Example of function usage:
   gen = prime_number_generator(10)
print(next(gen))  # 2
print(next(gen))  # 3
  root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = pre_order_traversal(root)
print(next(gen))  # 1
print(next(gen))  # 2

Task 7: Implement a generator for in-order traversal of a binary tree.
Create a generator function named in_order_traversal that takes the root of a binary tree and yields its nodes in in-order.
Example of function usage:
  root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = in_order_traversal(root)
print(next(gen))  # 2
print(next(gen))  # 1
Task 8: Write a generator for post-order traversal of a binary tree.
Create a generator function named post_order_traversal that takes the root of a binary tree and yields its nodes in post-order.
Example of function usage:
  root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
gen = post_order_traversal(root)
print(next(gen))  # 2
print(next(gen))  # 3
Task 9: Create a generator to traverse a graph using depth-first search (DFS).
Create a generator function named dfs_traversal that takes an adjacency list representation of a graph and a starting node, and yields nodes in DFS order.
Example of function usage:
  graph = {
    1: [2, 3],
2: [4],

     3: [5],
    4: [],
    5: []
}
gen = dfs_traversal(graph, 1)
print(next(gen))  # 1
print(next(gen))  # 2
Task 10: Develop a generator for breadth-first search (BFS) traversal of a graph.
Create a generator function named bfs_traversal that takes an adjacency list representation of a graph and a starting node, and yields nodes in BFS order.
Example of function usage:
  graph = {
    1: [2, 3],
    2: [4],
    3: [5],
    4: [],
    5: []
}
gen = bfs_traversal(graph, 1)
print(next(gen))  # 1
print(next(gen))  # 2
Task 11: Implement a generator that yields the keys of a dictionary.
Create a generator function named dict_keys_generator that takes a dictionary and yields its keys one by one.
Example of function usage:
Task 12: Write a generator that yields the values of a dictionary.
  gen = dict_keys_generator({'a': 1, 'b': 2, 'c': 3})
print(next(gen))  # 'a'
print(next(gen))  # 'b'

 Create a generator function named dict_values_generator that takes a dictionary and yields its values one by one.
Example of function usage:
Task 13: Create a generator to iterate over key-value pairs of a dictionary.
Create a generator function named dict_items_generator that takes a dictionary and yields its key-value pairs as tuples one by one.
Example of function usage:
Task 14: Develop a generator that yields lines from a file one by one.
Create a generator function named file_lines_generator that takes a file path and yields its lines one by one.
Example of function usage:
Task 15: Implement a generator to iterate over words in a text file.
Create a generator function named file_words_generator that takes a file path and yields its words one by one.
 gen = dict_values_generator({'a': 1, 'b': 2, 'c': 3})
print(next(gen))  # 1
print(next(gen))  # 2
  gen = dict_items_generator({'a': 1, 'b': 2, 'c': 3})
print(next(gen))  # ('a', 1)
print(next(gen))  # ('b', 2)
  gen = file_lines_generator('example.txt')
print(next(gen))  # 'First line'
print(next(gen))  # 'Second line'
 Example of function usage:

 gen = file_words_generator('example.txt')
print(next(gen))  # 'First'
print(next(gen))  # 'line'
Task 16: Write a generator that yields characters from a string one by one.
Create a generator function named string_chars_generator that takes a string and yields its characters one by one.
Example of function usage:
Task 17: Create a generator to yield unique elements from a list.
Create a generator function named unique_elements_generator that takes a list and yields its unique elements one by one.
Example of function usage:
Task 18: Develop a generator that yields elements of a list in reverse order.
Create a generator function named reverse_list_generator that takes a list and yields its elements in reverse order.
Example of function usage:
  gen = string_chars_generator('Hello')
print(next(gen))  # 'H'
print(next(gen))  # 'e'
  gen = unique_elements_generator([1, 2, 2, 3, 3, 3])
print(next(gen))  # 1
print(next(gen))  # 2
  gen = reverse_list_generator([1, 2, 3, 4, 5])
print(next(gen))  # 5
print(next(gen))  # 4

Task 19: Implement a generator to yield the Cartesian product of two lists.
Create a generator function named cartesian_product_generator that takes two lists and yields the Cartesian product of the two lists as tuples.
Example of function usage:
Task 20: Write a generator that yields permutations of a list.
Create a generator function named permutations_generator that takes a list and yields all possible permutations of the list.
Example of function usage:
Task 21: Create a generator to yield combinations of a list of elements.
Create a generator function named combinations_generator that takes a list of elements and yields all possible combinations of the elements.
Example of function usage:
Task 22: Develop a generator to iterate over a list of tuples.
  gen = cartesian_product_generator([1, 2], ['a', 'b'])
print(next(gen))  # (1, 'a')
print(next(gen))  # (1, 'b')
  gen = permutations_generator([1, 2, 3])
print(next(gen))  # (1, 2, 3)
print(next(gen))  # (1, 3, 2)
  gen = combinations_generator([1, 2, 3])
print(next(gen))  # (1,)
print(next(gen))  # (2,)

 Create a generator function named tuple_list_generator that takes a list of tuples and yields each tuple one by one.
Example of function usage:
Task 23: Implement a generator that yields elements from multiple lists in parallel.
Create a generator function named parallel_lists_generator that takes multiple lists and yields elements from each list in parallel.
Example of function usage:
Task 24: Write a generator that yields elements from a nested list (flattening the list).
Create a generator function named flatten_list_generator that takes a nested list and yields each element in a flat sequence.
Example of function usage:
Task 25: Create a generator to yield elements from a nested dictionary.
Create a generator function named nested_dict_generator that takes a nested dictionary and yields its elements.
 gen = tuple_list_generator([(1, 2), (3, 4), (5, 6)])
print(next(gen))  # (1, 2)
print(next(gen))  # (3, 4)
  gen = parallel_lists_generator([1, 2, 3], ['a', 'b', 'c'])
print(next(gen))  # (1, 'a')
print(next(gen))  # (2, 'b')
  gen = flatten_list_generator([1, [2, [3, 4], 5], 6])
print(next(gen))  # 1
print(next(gen))  # 2
 Example of function usage:

 gen = nested_dict_generator({'a': {'b': 1, 'c': 2}, 'd': 3})
print(next(gen))  # ('b', 1)
print(next(gen))  # ('c', 2)
Task 26: Develop a generator to yield powers of 2 up to a given number.
Create a generator function named powers_of_two_generator that takes an integer n and yields powers of 2 up to 2^n .
Example of function usage:
Task 27: Implement a generator that yields powers of a given base up to a specified limit.
Create a generator function named powers_of_base_generator that takes a base and a limit, and yields powers of the base up to the specified limit.
Example of function usage:
Task 28: Write a generator to yield the squares of numbers in a given range.
Create a generator function named squares_generator that takes a range of numbers and yields their squares.
Example of function usage:
  gen = powers_of_two_generator(4)
print(next(gen))  # 1
print(next(gen))  # 2
  gen = powers_of_base_generator(3, 81)
print(next(gen))  # 1
print(next(gen))  # 3
  gen = squares_generator(1, 5)
print(next(gen))  # 1
print(next(gen))  # 4

Task 29: Create a generator to yield cubes of numbers in a specified range.
Create a generator function named cubes_generator that takes a range of numbers and yields their cubes.
Example of function usage:
Task 30: Develop a generator that yields factorials of numbers up to a given limit.
Create a generator function named factorials_generator that takes an integer n and yields factorials of numbers from 0 up to n .
Example of function usage:
Task 31: Implement a generator to yield numbers in the Collatz sequence.
Create a generator function named collatz_sequence_generator that takes an integer and yields numbers in the Collatz sequence.
Example of function usage:
Task 32: Write a generator that yields numbers in a geometric progression.
  gen = cubes_generator(1, 4)
print(next(gen))  # 1
print(next(gen))  # 8
  gen = factorials_generator(4)
print(next(gen))  # 1
print(next(gen))  # 1
  gen = collatz_sequence_generator(6)
print(next(gen))  # 6
print(next(gen))  # 3

 Create a generator function named geometric_progression_generator that takes an initial term, a common ratio, and a limit, and yields numbers in the geometric progression.
Example of function usage:
Task 33: Create a generator to yield numbers in an arithmetic progression.
Create a generator function named arithmetic_progression_generator that takes an initial term, a common difference, and a limit, and yields numbers in the arithmetic progression.
Example of function usage:
Task 34: Develop a generator that yields the running sum of a list of numbers.
Create a generator function named running_sum_generator that takes a list of numbers and yields their running sum.
Example of function usage:
Task 35: Implement a generator to yield the running product of a list of numbers.
Create a generator function named running_product_generator that takes a list of numbers and yields their running product.
 gen = geometric_progression_generator(2, 3, 20)
print(next(gen))  # 2
print(next(gen))  # 6
  gen = arithmetic_progression_generator(2, 3, 20)
print(next(gen))  # 2
print(next(gen))  # 5
  gen = running_sum_generator([1, 2, 3, 4])
print(next(gen))  # 1
print(next(gen))  # 3
 
Example of function usage:
gen = running_product_generator([1, 2, 3, 4])
print(next(gen))  # 1
print(next(gen))  # 2

```
___
Виконання роботи:
```Python
# Task 1
def number_generator(numbers):
    for num in numbers:
        yield num

# Task 2
def even_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num

# Task 3
def odd_number_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            yield num

# Task 4
def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Task 5
def prime_number_generator(limit):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    for num in range(2, limit + 1):
        if is_prime(num):
            yield num

# Task 6, 7, 8 (Binary Tree Traversals)
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def pre_order_traversal(root):
    if root:
        yield root.val
        yield from pre_order_traversal(root.left)
        yield from pre_order_traversal(root.right)

def in_order_traversal(root):
    if root:
        yield from in_order_traversal(root.left)
        yield root.val
        yield from in_order_traversal(root.right)

def post_order_traversal(root):
    if root:
        yield from post_order_traversal(root.left)
        yield from post_order_traversal(root.right)
        yield root.val

# Task 9 (DFS Traversal)
def dfs_traversal(graph, start):
    visited = set()
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            yield node
            visited.add(node)
            stack.extend(reversed(graph[node]))

# Task 10 (BFS Traversal)
from collections import deque

def bfs_traversal(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            yield node
            visited.add(node)
            queue.extend(graph[node])

# Task 11, 12, 13 (Dictionary Generators)
def dict_keys_generator(d):
    for key in d.keys():
        yield key

def dict_values_generator(d):
    for value in d.values():
        yield value

def dict_items_generator(d):
    for item in d.items():
        yield item

# Task 14, 15 (File Generators)
def file_lines_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line.strip()

def file_words_generator(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            for word in line.split():
                yield word

# Task 16 (String Generator)
def string_chars_generator(string):
    for char in string:
        yield char

# Task 17 (Unique Elements Generator)
def unique_elements_generator(lst):
    seen = set()
    for item in lst:
        if item not in seen:
            yield item
            seen.add(item)

# Task 18 (Reverse List Generator)
def reverse_list_generator(lst):
    for item in reversed(lst):
        yield item

# Task 19 (Cartesian Product Generator)
def cartesian_product_generator(lst1, lst2):
    for item1 in lst1:
        for item2 in lst2:
            yield (item1, item2)

# Task 20 (Permutations Generator)
from itertools import permutations

def permutations_generator(lst):
    for perm in permutations(lst):
        yield perm

# Task 21 (Combinations Generator)
from itertools import combinations

def combinations_generator(lst):
    for i in range(1, len(lst) + 1):
        for comb in combinations(lst, i):
            yield comb

# Task 22 (Tuple List Generator)
def tuple_list_generator(tuples):
    for tup in tuples:
        yield tup

# Task 23 (Parallel Lists Generator)
def parallel_lists_generator(*lists):
    for items in zip(*lists):
        yield items

# Task 24 (Flatten List Generator)
def flatten_list_generator(nested_list):
    for item in nested_list:
        if isinstance(item, list):
            yield from flatten_list_generator(item)
        else:
            yield item

# Task 25 (Nested Dictionary Generator)
def nested_dict_generator(d):
    for key, value in d.items():
        if isinstance(value, dict):
            yield from nested_dict_generator(value)
        else:
            yield (key, value)

# Task 26 (Powers of Two Generator)
def powers_of_two_generator(n):
    for i in range(n + 1):
        yield 2 ** i

# Task 27 (Powers of Base Generator)
def powers_of_base_generator(base, limit):
    power = 1
    while power <= limit:
        yield power
        power *= base

# Task 28 (Squares Generator)
def squares_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 2

# Task 29 (Cubes Generator)
def cubes_generator(start, end):
    for num in range(start, end + 1):
        yield num ** 3

# Task 30 (Factorials Generator)
def factorials_generator(n):
    factorial = 1
    for i in range(n + 1):
        if i == 0:
            yield 1
        else:
            factorial *= i
            yield factorial

# Task 31 (Collatz Sequence Generator)
def collatz_sequence_generator(n):
    while n != 1:
        yield n
        n = n // 2 if n % 2 == 0 else 3 * n + 1
    yield 1

# Task 32 (Geometric Progression Generator)
def geometric_progression_generator(initial, ratio, limit):
    current = initial
    while current <= limit:
        yield current
        current *= ratio

# Task 33 (Arithmetic Progression Generator)
def arithmetic_progression_generator(initial, difference, limit):
    current = initial
    while current <= limit:
        yield current
        current += difference

# Task 34 (Running Sum Generator)
def running_sum_generator(numbers):
    total = 0
    for num in numbers:
        total += num
        yield total

# Task 35 (Running Product Generator)
def running_product_generator(numbers):
    product = 1
    for num in numbers:
        product *= num
        yield product

```
___
Результати:
```Python
[1, 2, 3, 4]
[2, 4, 6, 8, 10]
[1, 3, 5, 7, 9]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
[2, 3, 5, 7, 11, 13, 17, 19]
[1, 2, 4, 5, 3]
[4, 2, 5, 1, 3]
[4, 5, 2, 3, 1]
['A', 'B', 'D', 'E', 'F', 'C']
['A', 'B', 'C', 'D', 'E', 'F']
['a', 'b', 'c']
[1, 2, 3]
[('a', 1), ('b', 2), ('c', 3)]

```
___
Висновки:Виконання даної лабораторної роботи дозволило значно поглибити розуміння та навички роботи з генераторами в мові програмування Python. Генератори є потужним інструментом для створення ітераторів, що забезпечують ефективне використання пам'яті та підвищення продуктивності програм. Я навчилася створювати різні типи генераторів для роботи з числами, словниками, текстовими файлами, графами та деревами, а також генерувати числові послідовності та комбінації елементів. Цей досвід наочно продемонстрував переваги використання генераторів для обробки великих обсягів даних та реалізації складних алгоритмів.