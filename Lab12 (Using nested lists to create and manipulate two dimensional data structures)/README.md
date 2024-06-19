Лабораторна робота №12: Using nested lists to create and manipulate two-dimensional data structures
___
Мета роботи:
Метою цієї лабораторної роботи є ознайомлення з основами роботи з двовимірними масивами та об'єктно-орієнтованим програмуванням у Python.Ця лабораторна робота допоможе розвинути навички роботи з матрицями, зрозуміти основи об'єктно-орієнтованого підходу до програмування та застосовувати методи класів для реалізації різноманітних операцій з матрицями.
___
Опис завдання:
```Python
Task 1: Create a Matrix
Create a Python class Matrix that initializes a two-dimensional list with zeros.
The constructor should accept two parameters: rows and columns, indicating the
dimensions of the matrix.
Example of class usage:matrix = Matrix(2, 3)
print(matrix.data) # [[0, 0, 0], [0, 0, 0]]
Task 2: Add Elements to Matrix
Extend the Matrix class by adding a method add_element that adds an element
at a specific position (row, column).
Example of class usage:matrix = Matrix(2, 3)
matrix.add_element(1, 2, 10)
print(matrix.data) # [[0, 0, 10], [0, 0, 0]]
Task 3: Sum of Rows
Add a method sum_of_rows to the Matrix class that returns a list of sums of
each row in the matrix.
Example of class usage:matrix = Matrix(2, 3)
matrix.add_element(0, 0, 5)
matrix.add_element(0, 1, 10)
matrix.add_element(1, 2, 20)
print(matrix.sum_of_rows()) # [15, 20]
Task 4: Matrix Transposition
Create a method transpose in the Matrix class that returns a new Matrix
object, which is the transpose of the original matrix.
Example of class usage:matrix = Matrix(2, 3)
matrix.add_element(0, 1, 1)
matrix.add_element(1, 2, 2)
transposed = matrix.transpose()
print(transposed.data) # [[0, 0], [1, 0], [0, 2]]
Task 5: Multiply Matrices
Implement a method multiply_by in the Matrix class that accepts another
Matrix object and returns a new Matrix object that is the result of the multiplication
of the two matrices.
Example of class usage:matrix1 = Matrix(2, 3)
matrix1.add_element(0, 0, 1)
matrix1.add_element(0, 1, 2)
matrix1.add_element(0, 2, 3)
matrix2 = Matrix(3, 2)
matrix2.add_element(0, 0, 1)
matrix2.add_element(1, 0, 2)
matrix2.add_element(2, 0, 3)
result = matrix1.multiply_by(matrix2)
print(result.data) # [[14, 0], [0, 0]]
Task 6: Check Symmetric Matrix
Add a method is_symmetric to the Matrix class that checks if the matrix is
symmetric (i.e., the matrix is equal to its transpose).
Example of class usage:matrix = Matrix(2, 2)
matrix.add_element(0, 1, 5)
matrix.add_element(1, 0, 5)
print(matrix.is_symmetric()) # True
Task 7: Rotate Matrix
Implement a method rotate_right in the Matrix class that rotates the matrix
90 degrees to the right.
Example of class usage:matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
matrix.rotate_right()
print(matrix.data) # [[3, 1], [4, 2]]
Task 8: Flatten Matrix
Create a method flatten in the Matrix class that returns a single list containing
all elements of the matrix.
Example of class usage:matrix = Matrix(2, 2)
matrix.add_element(0, 0, 1)
matrix.add_element(0, 1, 2)
matrix.add_element(1, 0, 3)
matrix.add_element(1, 1, 4)
print(matrix.flatten()) # [1, 2, 3, 4]
Task 9: Matrix from List
Add a static method from_list to the Matrix class that creates a matrix object
from a given list of lists.
Example of class usage:
python
list_of_lists = [[1, 2], [3, 4]]
matrix = Matrix.from_list(list_of_lists)
print(matrix.data) # [[1, 2], [3, 4]]
Task 10: Extract Diagonal
Create a method diagonal in the Matrix class that extracts the diagonal of a
square matrix as a list.
Example of class usage:matrix = Matrix(3, 3)
matrix.add_element(0, 0, 1)
matrix.add_element(1, 1, 2)
matrix.add_element(2, 2, 3)
print(matrix.diagonal()) # [1, 2, 3]


```
___
Виконання роботи:
```Python
class Matrix:
    def __init__(self, rows, columns, data=None):
        self.rows = rows
        self.columns = columns
        if data is None:
            self.data = [[0] * columns for _ in range(rows)]
        else:
            self.data = data


    def add_element(self, row, column, value):
        if 0 <= row < self.rows and 0 <= column < self.columns:
            self.data[row][column] = value
        else:
            print("Invalid position.")

    def sum_of_rows(self):
        return [sum(self.data[row]) for row in range(self.rows)]

    def transpose(self):
        transposed_data = [[self.data[j][i] for j in range(self.rows)] for i in range(self.columns)]
        return Matrix(self.columns, self.rows, transposed_data)

    def multiply_by(self, other):
        if self.columns != other.rows:
            print("Cannot multiply matrices: incompatible sizes.")
            return None

        result = Matrix(self.rows, other.columns)
        for i in range(self.rows):
            for j in range(other.columns):
                for k in range(self.columns):
                    result.data[i][j] += self.data[i][k] * other.data[k][j]
        return result

    def is_symmetric(self):
        return self.data == self.transpose().data

    def rotate_right(self):
        rotated_data = [[self.data[self.rows - 1 - j][i] for j in range(self.rows)] for i in range(self.columns)]
        self.data = rotated_data
        self.rows, self.columns = self.columns, self.rows

    def flatten(self):
        return [element for row in self.data for element in row]

    @staticmethod
    def from_list(list_of_lists):
        rows = len(list_of_lists)
        columns = len(list_of_lists[0])
        matrix = Matrix(rows, columns)
        for i in range(rows):
            for j in range(columns):
                matrix.data[i][j] = list_of_lists[i][j]
        return matrix

    def diagonal(self):
        if self.rows != self.columns:
            print("Matrix must be square.")
            return None
        return [self.data[i][i] for i in range(self.rows)]



# Приклади виклику функцій з очікуваним виводом
matrix1 = Matrix(3, 3)
print(matrix1.data)

matrix1.add_element(1, 1, 5)
print(matrix1.data)

sum_rows = matrix1.sum_of_rows()
print(sum_rows)

transposed_matrix = matrix1.transpose()
print(transposed_matrix.data)

matrix2 = Matrix.from_list([[1, 2], [3, 4], [5, 6]])
result_matrix = matrix1.multiply_by(matrix2)
print(result_matrix.data if result_matrix else "Cannot multiply matrices")

print(matrix1.is_symmetric())

matrix1.rotate_right()
print(matrix1.data)

flattened_matrix = matrix1.flatten()
print(flattened_matrix)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix3 = Matrix.from_list(list_of_lists)
print(matrix3.data)

diagonal_elements = matrix3.diagonal()
print(diagonal_elements)




```
___
Результати:
```Python
[[0, 0, 0], [0, 0, 0], [0, 0, 0]]
[[0, 0, 0], [0, 5, 0], [0, 0, 0]]
[0, 5, 0]
[[0, 0, 0], [0, 5, 0], [0, 0, 0]]
[[0, 0], [15, 20], [0, 0]]
True
[[0, 0, 0], [0, 5, 0], [0, 0, 0]]
[0, 0, 0, 0, 5, 0, 0, 0, 0]
[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[1, 5, 9]

```
___
Висновки:В ході виконання цієї лабораторної роботи я ознайомилася з основними принципами роботи з двовимірними масивами та об'єктно-орієнтованим програмуванням у Python. Я реалізувала клас Matrix, який дозволяє працювати з матрицями різними способами. Загалом, виконання цієї лабораторної роботи допомогло мені значно розширити знання та практичні навички у роботі з матрицями та об'єктно-орієнтованим програмуванням у Python.