from typing import Union


class Shop:

    def __init__(self, shop_name: str) -> None:
        self.shop_name = shop_name
        self.goods = []

    def add_product(self, product) -> None:
        self.goods.append(product)

    def remove_product(self, product) -> None:
        self.goods.remove(product)


class Product:
    __id = 0

    def __new__(cls, *args, **kwargs):
        cls.__id += 1
        return super().__new__(cls)

    def __init__(self, name: str, weight: int, price: Union[int, float]) -> None:
        self.id = self.__id
        self.name = name
        self.weight = weight
        self.price = price

    def __setattr__(self, key, value):
        if key == 'id' and type(value) == int:
            object.__setattr__(self, key, value)

        elif key == 'name' and type(value) == str:
            object.__setattr__(self, key, value)

        elif key == 'weight' and type(value) == int and value > 0:
            object.__setattr__(self, key, value)

        elif key == 'price' and isinstance(value, (int, float)) and value > 0:
            object.__setattr__(self, key, value)
        else:
            raise TypeError("Неверный тип присваиваемых данных")

    def __delattr__(self, item):
        if item == 'id':
            raise AttributeError("Атрибут id удалять запрещено.")
        object.__delattr__(self, item)



prod = Product('name', 1, 2.2)
pr = Product('NAME', 2, 3)

del pr.name
print(pr.__dict__)
