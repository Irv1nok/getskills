from typing import Union
from math import sqrt


class VerifyData:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name, None)

    def __set__(self, instance, value):
        if value <= 0 or not isinstance(value, (int, float)):
            raise ValueError("длины сторон треугольника должны быть положительными числами")
        setattr(instance, self.name, value)


class Triangle:
    a = VerifyData()
    b = VerifyData()
    c = VerifyData()

    def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]):
        self.triangle_check(a, b, c)
        self.a = a
        self.b = b
        self.c = c

    def triangle_check(self, a, b, c):
        if not (a < b + c) or not (b < a + c) or not (c < a + b):
            raise ValueError("с указанными длинами нельзя образовать треугольник")

    def __len__(self) -> int:
        return int(self.a + self.b + self.c)

    def __call__(self) -> Union[int, float]:
        p = len(self) / 2
        return sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


tr = Triangle(5, 4, 3)
assert tr.a == 5 and tr.b == 4 and tr.c == 3, "дескрипторы вернули неверные значения"

try:
    tr = Triangle(-5, 4, 3)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

try:
    tr = Triangle(10, 1, 1)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

tr = Triangle(5, 4, 3)
assert len(tr) == 12, "функция len вернула неверное значение"
assert 5.9 < tr() < 6.1, "метод __call__ вернул неверное значение"
