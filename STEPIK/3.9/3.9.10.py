from typing import Union, Tuple


class Matrix:

    def __init__(self, *args: tuple):
        if len(args) == 3:
            self.rows, self.cols, self.fill_value = args
            self.table = [[self.fill_value for _ in range(self.cols)] for _ in range(self.rows)]
        else:
            self.table = args[0]
            self.rows = len(self.table)
            self.cols = len(self.table[0])

        self.check_table_size(self.table)

    def __setattr__(self, key: Tuple[int, int], value: Union[int, float]):
        if type(value) == list:
            object.__setattr__(self, key, value)

        elif type(value) not in (int, float):
            raise TypeError('аргументы rows, cols - целые числа; fill_value - произвольное число')

        else:
            object.__setattr__(self, key, value)

    def check_table_size(self, table):
        if not all([len(table[0]) == len(row) for row in table]) \
                or not all([type(j) == int for i in table for j in i]):
            raise TypeError('список должен быть прямоугольным, состоящим из чисел')

    def check_indx(self, i: Tuple[int, int]):
        if not 0 <= i[0] <= (self.rows - 1) \
                or not 0 <= i[1] <= (self.cols - 1):
            raise IndexError('недопустимые значения индексов')

    def check_type_data(self, value: Union[int, float]):
        if type(value) not in (int, float):
            raise TypeError('значения матрицы должны быть числами')

    def __getitem__(self, key: Tuple[int, int]):
        self.check_indx(key)
        i, j = key
        return self.table[i][j]

    def __setitem__(self, key: Tuple[int, int], value: Union[int, float]):
        self.check_indx(key)
        self.check_type_data(value)
        i, j = key
        self.table[i][j] = value

    def __add__(self, other: "Matrix"):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')

        obj = other if isinstance(other, (int, float)) else other.table

        res = []
        for i, x in enumerate(self.table):

            if isinstance(obj, list):
                res.append([x[j] + obj[i][j] for j in range(len(x))])
            else:
                res.append([x[j] + obj for j in range(len(x))])

        return Matrix(res)

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.rows != other.rows or self.cols != other.cols:
                raise ValueError('операции возможны только с матрицами равных размеров')

        obj = other if isinstance(other, (int, float)) else other.table

        res = []
        for i, x in enumerate(self.table):

            if isinstance(obj, list):
                res.append([x[j] - obj[i][j] for j in range(len(x))])
            else:
                res.append([x[j] - obj for j in range(len(x))])

        return Matrix(res)


list2D = [[1, 2], [3, 4], [5, 6, 7]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не прямоугольного списка в конструкторе Matrix"

list2D = [[1, []], [3, 4], [5, 6]]
try:
    st = Matrix(list2D)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для списка не из чисел в конструкторе Matrix"

try:
    st = Matrix('1', 2, 0)
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError для не числовых аргументов в конструкторе Matrix"

list2D = [[1, 2], [3, 4], [5, 6]]
matrix = Matrix(list2D)
assert matrix[2, 1] == 6, "неверно отработал конструктор или __getitem__"

matrix = Matrix(4, 5, 10)
assert matrix[3, 4] == 10, "неверно отработал конструктор или __getitem__"

try:
    v = matrix[3, -1]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

# try:
#     v = matrix['0', 4]
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"

matrix[0, 0] = 7
assert matrix[0, 0] == 7, "неверно отработал __setitem__"

try:
    matrix[0, 0] = 'a'
except TypeError:
    assert True
else:
    assert False, "не сгенерировалось исключение TypeError в __setitem__"

# m1 = Matrix([[1, 2], [3, 4]])
# m2 = Matrix([[1, 1], [1, 1], [1, 1]])
#
# try:
#     matrix = m1 + m2
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError при сложении матриц разных размеров"

m1 = Matrix([[1, 2], [3, 4]])
m2 = Matrix([[1, 1], [1, 1]])
matrix = m1 + m2
assert isinstance(matrix, Matrix), "операция сложения матриц должна возвращать экземпляр класса Matrix"
assert matrix[1, 1] == 5, "неверно отработала операция сложения матриц"
assert m1[1, 1] == 4 and m1[0, 1] == 2 and m2[1, 1] == 1 \
       and m2[0, 0] == 1, "исходные матрицы не должны меняться при операции сложения"

m1 = Matrix(2, 2, 1)
id_m1_old = id(m1)
m2 = Matrix(2, 2, 1)
m1 = m1 + m2
id_m1_new = id(m1)
assert id_m1_old != id_m1_new, "в результате операции сложения должен создаваться НОВЫЙ экземпляр класса Matrix"

matrix = Matrix(2, 2, 0)
m = matrix + 10
assert matrix[0, 0] == matrix[1, 1] == 0, "исходные матрицa не должна меняться при операции сложения c числом"
assert m[0, 0] == 10, "неверно отработала операция сложения матрицы с числом"

m1 = Matrix(2, 2, 1)
m2 = Matrix([[0, 1], [1, 0]])
identity_matrix = m1 - m2  # должна получиться единичная матрица
assert m1[0, 0] == 1 and m1[1, 1] == 1 and m2[0, 0] == 0 \
       and m2[0, 1] == 1, "исходные матрицы не должны меняться при операции вычитания"
assert identity_matrix[0, 0] == 1 and identity_matrix[1, 1] == 1, "неверно отработала операция вычитания матриц"

matrix = Matrix(2, 2, 1)
m = matrix - 1
assert matrix[0, 0] == matrix[1, 1] == 1, "исходные матрицa не должна меняться при операции вычитания c числом"
assert m[0, 0] == m[1, 1] == 0, "неверно отработала операция вычитания числа из матрицы"
