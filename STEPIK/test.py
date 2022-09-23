class MaxPooling:
    def __init__(self, step=(2, 2), size=(2, 2)):
        self.step = step
        self.size = size

    def __call__(self, lst):
        self._check(lst)
        out = []
        for i in range(0, len(lst) - self.size[1] + 1, self.step[1]):
            out.append([])
            for j in range(0, len(lst[i]) - self.size[0] + 1, self.step[0]):
                out[-1].append(max(v2 for v1 in lst[i: i+self.size[1]] for v2 in v1[j: j+self.size[0]]))
        return(out)

    def _check(self, lst):
        if (
            len(set(map(len, lst))) > 1 or any(type(v2) not in (int, float) for v1 in lst for v2 in v1)
        ):
            raise ValueError("Неверный формат для первого параметра matrix.")


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
