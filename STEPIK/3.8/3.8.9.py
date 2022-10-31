from typing import Union


class Bag:

    def __init__(self, max_weight: int):
        self.max_weight = max_weight
        self.put_into = []

    def _check_weight(self, thing: "Thing"):
        if sum(map(lambda x: x.weight, self.put_into), thing.weight) > self.max_weight:
            raise ValueError('превышен суммарный вес предметов')

    def _check_idx(self, i: int):
        if i > len(self.put_into):
            raise IndexError('неверный индекс')

    def add_thing(self, thing: "Thing"):
        self._check_weight(thing)
        self.put_into.append(thing)

    def __getitem__(self, item: int) -> "Thing":
        self._check_idx(item)
        return self.put_into[item]

    def __setitem__(self, key: int, new_value: "Thing"):
        self._check_idx(key)
        self.__delitem__(key)
        self._check_weight(new_value)
        self.put_into.insert(key, new_value)

    def __delitem__(self, key: int):
        self._check_idx(key)
        del self.put_into[key]


class Thing:

    def __init__(self, name: str, weight: Union[int, float]):
        self.name = name
        self.weight = weight


b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

try:
    b.add_thing(Thing('рубашка', 500))
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError"

assert b[0].name == 'книга' and b[
    0].weight == 100, "атрибуты name и weight объекта класса Thing принимают неверные значения"

t = Thing('Python', 20)
b[1] = t
assert b[1].name == 'Python' and b[
    1].weight == 20, "неверные значения атрибутов name и weight, возможно, некорректно работает оператор присваивания с объектами класса Thing"

del b[0]
assert b[0].name == 'Python' and b[0].weight == 20, "некорректно отработал оператор del"

try:
    t = b[2]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

b = Bag(700)
b.add_thing(Thing('книга', 100))
b.add_thing(Thing('носки', 200))

b[0] = Thing('рубашка', 500)

try:
    b[0] = Thing('рубашка', 800)
except ValueError:
    assert True
else:
    assert False, "не сгенерировалось исключение ValueError при замене предмета в объекте класса Bag по индексу"