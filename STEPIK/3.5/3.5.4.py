from typing import Union


class Dimensions:
    MIN_DIMENSION = 10
    MAX_DIMENSION = 10_000

    def __init__(self, a: int, b: int, c: int) -> None:
        self.a = a
        self.b = b
        self.c = c

    @classmethod
    def check_dimension(cls, value: int) -> bool:
        return value if cls.MIN_DIMENSION <= value <= cls.MAX_DIMENSION else False

    def calc_dimension(self) -> int:
        return self.a * self.b * self.c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value):
        if self.check_dimension(value):
            self.__a = value

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value):
        if self.check_dimension(value):
            self.__b = value

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value):
        if self.check_dimension(value):
            self.__c = value

    def __lt__(self, other: "Dimensions") -> bool:
        return True if self.calc_dimension() < other.calc_dimension() else False

    def __le__(self, other: "Dimensions") -> bool:
        return True if self.calc_dimension() <= other.calc_dimension() else False


class ShopItem:

    def __init__(self, name: str, price: Union[int, float], dim: "Dimensions") -> None:
        self.name = name
        self.price = price
        self.dim = dim


lst_shop = [ShopItem("кеды", 1024, Dimensions(40, 30, 120)),
            ShopItem("зонт", 500.24, Dimensions(10, 20, 50)),
            ShopItem("холодильник", 40_000, Dimensions(2000, 600, 500)),
            ShopItem("табуретка", 2000.99, Dimensions(500, 200, 200))]
lst_shop_sorted = sorted(lst_shop, key=lambda x: x.dim)
print(lst_shop)
print(lst_shop_sorted)
