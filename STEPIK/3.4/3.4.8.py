from typing import Union

class Item:

    def __init__(self, name: str, money: Union[int, float]) -> None:
        self.name = name if type(name) == str else ''
        self.money = money if type(money) in (int, float) else None

    def __add__(self, other: "Item") -> int:
        return self.money + other

    def __radd__(self, other: int) -> int:
        return other + self.money

class Budget:

    def __init__(self) -> None:
        self.list_items = []

    def add_item(self, it: "Item") -> None:
        self.list_items.append(it)

    def remove_item(self, indx: int) -> None:
        self.list_items.pop(indx)

    def get_items(self) -> list:
        return self.list_items


my_budget = Budget()
my_budget.add_item(Item("Курс по Python ООП", 2000))
my_budget.add_item(Item("Курс по Django", 5000.01))
my_budget.add_item(Item("Курс по NumPy", 0))
my_budget.add_item(Item("Курс по C++", 1500.10))

# вычисление общих расходов
s = 0
for x in my_budget.get_items():
    s = s + x