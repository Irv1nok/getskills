from typing import Union


class RadiusVector2D:
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x: Union[int, float] = 0, y: Union[int, float] = 0) -> None:
        self.__x = x if self.check_value(x) else 0
        self.__y = y if self.check_value(y) else 0

    @classmethod
    def check_value(cls, arg: Union[int, float]) -> bool:
        return type(arg) in (int, float) and cls.MIN_COORD < arg < cls.MAX_COORD

    @property
    def x(self) -> Union[int, float]:
        return self.__x

    @x.setter
    def x(self, coord: Union[int, float]) -> None:
        if self.check_value(coord):
            self.__x = coord

    @property
    def y(self) -> Union[int, float]:
        return self.__y

    @y.setter
    def y(self, coord: Union[int, float]) -> None:
        if self.check_value(coord):
            self.__y = coord

    @staticmethod
    def norm2(vector: "RadiusVector2D") -> Union[int, float]:
        x = vector.x
        y = vector.y
        return (x * x) + (y * y)


r1 = RadiusVector2D()
r2 = RadiusVector2D(1)
r3 = RadiusVector2D(4, 5)

assert hasattr(RadiusVector2D, 'MIN_COORD') and hasattr(RadiusVector2D,
                                                        'MAX_COORD'), "в классе RadiusVector2D должны присутствовать атрибуты MIN_COORD и MAX_COORD"

assert type(RadiusVector2D.x) == property and type(
    RadiusVector2D.y) == property, "в классе RadiusVector2D должны присутствовать объекты-свойства x и y"

assert r1.x == 0 and r1.y == 0 and r2.x == 1 and r2.y == 0 and r3.x == 4 and r3.y == 5, "свойства x и y возвращают неверные значения"

assert RadiusVector2D.norm2(r3) == 41, "неверно вычисляется норма вектора"

r4 = RadiusVector2D(4.5, 5.5)
assert 4.4 < r4.x < 4.6 and 5.4 < r4.y < 5.6, "свойства x и y возвращают неверные значения"

r5 = RadiusVector2D(-102, 2000)
print(r5.__dict__)
assert r5.x == 0 and r5.y == 0, "присвоение значений, выходящих за диапазон [-100; 1024] не должно выполняться"

r = RadiusVector2D(10, 20)
print(r.__dict__)
r.x = 'a'
print(r.__dict__)
r.y = (1, 2)
print(r.__dict__)
assert r.x == 10 and r.y == 20, "присвоение не числовых значений должно игнорироваться"
