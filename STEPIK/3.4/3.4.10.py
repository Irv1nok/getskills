import copy


class MaxPooling:

    def __init__(self, step: tuple = (2, 2), size: tuple = (2, 2)) -> None:
        self.step = step if len(step) == 2 and all(map(lambda x: type(x) is int, step)) else (2, 2)
        self.size = size if len(size) == 2 and all(map(lambda y: type(y) is int, size)) else (2, 2)

    def __call__(self, matrix: list) -> list:
        if self.check_val_matrix(matrix):
            cpy_matrix = copy.deepcopy(matrix)
            x, y = self.size
            width, hight = self.step

            max_pool = []
            op_res = []
            for i in range(0, len(matrix), hight):
                try:
                    for _ in range(0, len(matrix), width):
                        max_pool.append(list(map(max, cpy_matrix[i][:x], cpy_matrix[i+1][:x])))
                        del cpy_matrix[i][:width]
                        del cpy_matrix[i+1][:width]

                    op_res.append(max_pool[:x])
                    del max_pool[:x]
                except IndexError:
                    break

            for n in range(len(op_res)):
                for j in range(len(op_res[n])):
                    if len(op_res[n][j]) >= x:
                        op_res[n][j] = max(op_res[n][j])
                    else:
                        del op_res[n][j]
            return op_res

    @staticmethod
    def check_val_matrix(matrix: list) -> bool:
        if not all([False if type(y) not in (int, float) else True for x in matrix for y in x]):
            raise ValueError("Неверный формат для первого параметра matrix.")
        elif not len(matrix) > 1 or not len(matrix[0]) > 1:
            raise ValueError("Неверный формат для первого параметра matrix.")
        elif not all([len(matrix[x]) == len(matrix[x+1]) for x in range(len(matrix) - 1)]):
            raise ValueError("Неверный формат для первого параметра matrix.")
        else:
            return True


mp = MaxPooling(step=(2, 2), size=(2,2))
m1 = [[1, 10, 10], [5, 10, 0], [0, 1, 2]]
m2 = [[1, 10, 10, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res1 = mp(m1)
res2 = mp(m2)

assert res1 == [[10]], "неверный результат операции MaxPooling"
assert res2 == [[10, 12], [40, 300]], "неверный результат операции MaxPooling"

mp = MaxPooling(step=(3, 3), size=(2,2))
m3 = [[1, 12, 14, 12], [5, 10, 0, -5], [0, 1, 2, 300], [40, -100, 0, 54.5]]
res3 = mp(m3)
assert res3 == [[12]], "неверный результат операции при MaxPooling(step=(3, 3), size=(2,2))"

try:
    res = mp([[1, 2], [3, 4, 5]])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не прямоугольную матрицу"

try:
    res = mp([[1, 2], [3, '4']])
except ValueError:
    assert True
else:
    assert False, "некорректо отработала проверка (или она отсутствует) на не числовые значения в матрице"




