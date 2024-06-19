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