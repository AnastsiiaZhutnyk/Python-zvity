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


