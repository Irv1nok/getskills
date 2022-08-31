from typing import Any, Union


class Circle:

    def __init__(self, x: Union[int, float], y: Union[int, float], radius: Union[int, float]) -> None:
        self.__x = x
        self.__y = y
        self.__radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def __setattr__(self, key: str, value: Union[int, float]) -> None:
        if type(value) not in (int, float):
            raise TypeError("Неверный тип присваиваемых данных.")
        elif key == 'radius' and value < 0:
            pass

        else:
            object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False


circle = Circle(10.5, 7, 22)
circle.radius = -10  # прежнее значение не должно меняться, т.к. отрицательный радиус недопустим
print(circle.radius)
x, y = circle.x, circle.y
res = circle.name  # False, т.к. атрибут name не существует
print(res)
print(circle.__dict__)
