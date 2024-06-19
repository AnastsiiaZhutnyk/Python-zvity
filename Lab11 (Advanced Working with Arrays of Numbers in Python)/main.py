from collections import Counter


def task1(n):
    return sum(x ** 2 for x in n)


def task2(arr):
    avg = sum(arr) / len(arr)
    return sum(x for x in arr if x >= avg)


def task3(arr):
    frequency = Counter(arr)
    sorted_array = sorted(arr, key=lambda x: (-frequency[x], x))
    return sorted_array


def task4(arr):
    n = len(arr) + 1
    totals = n * (n + 1) // 2
    sum_array = sum(arr)
    return totals - sum_array


def task5(number):
    nums = set(number)
    ls = 0
    for num in nums:
        if num - 1 not in nums:
            curent = num
            current = 1
            while curent + 1 in nums:
                curent += 1
                current += 1
            ls = max(ls, current)
    return ls


def task6(arrrr, s):
    s %= len(arrrr)
    arrrr[:] = arrrr[-s:] + arrrr[:-s]
    return arrrr


def task7(numbers):
    x = len(numbers)
    left_products = [1] * x
    right_products = [1] * x
    result = [1] * x
    for i in range(1, x):
        left_products[i] = left_products[i - 1] * numbers[i - 1]
    for i in range(x - 2, -1, -1):
        right_products[i] = right_products[i + 1] * numbers[i + 1]
    for i in range(x):
        result[i] = left_products[i] * right_products[i]
    return result


def task8(numbers):
    maxsum = float('-inf')
    currents = 0
    for num in numbers:
        currents = max(num, currents + num)
        maxsum = max(maxsum, currents)
    return maxsum


def task9(matrix):
    if not matrix:
        return []
    result = []
    top, bottom, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
    while top <= bottom and left <= right:

        for col in range(left, right + 1):
            result.append(matrix[top][col])
        top += 1

        for row in range(top, bottom + 1):
            result.append(matrix[row][right])
        right -= 1

        if top <= bottom:
            for col in range(right, left - 1, -1):
                result.append(matrix[bottom][col])
            bottom -= 1

        if left <= right:
            for row in range(bottom, top - 1, -1):
                result.append(matrix[row][left])
            left += 1
    return result


def task10(point, n):
    dis = [(x ** 2 + y ** 2, (x, y)) for x, y in point]

    dis.sort()
    return [point for _, point in dis[:n]]


# Приклади виклику функцій з очікуваним виводом
print(task1([1, 2, 3, 4]))
print(task2([1, 2, 3, 4, 5]))
print(task3([4, 5, 6, 5, 4, 3]))
print(task4([1, 2, 4, 5]))
print(task5([100, 4, 200, 1, 3, 2]))
print(task6([1, 2, 3, 4, 5], 2))
print(task7([1, 2, 3, 4]))
print(task8([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(task9([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
points = [(1, 2), (2, 3), (3, 4), (1, -1)]
n = 2
print(task10(points, n))
