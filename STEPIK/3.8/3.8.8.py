from typing import Union


class Cell:

    def __init__(self):
        self.is_free = False
        self.value = 0

    def __bool__(self):
        return True if self.is_free else False

    def __repr__(self):
        return f"{self.value}"


class TicTacToe:

    def __init__(self):
        self.pole = self.clear()

    def clear(self):
        self.pole = tuple([Cell() for _ in range(3)] for _ in range(3))
        return self

    def __getitem__(self, item):
        try:
            if slice in map(type, item):
                if type(item[0]) == int:
                    return tuple(map(lambda x: x.value, self.pole[item[0]]))
                else:
                    return tuple(map(lambda x: x[item[1]].value, self.pole[item[0]]))

            return self.pole[item[0]][item[1]].value
        except IndexError:
            raise IndexError('неверный индекс клетки')

    def __setitem__(self, key: int, value: Union[int, float]):
        try:
            if self.pole[key[0]][key[1]].value:
                raise ValueError('клетка уже занята')

            self.pole[key[0]][key[1]].value = value

        except IndexError:
            raise IndexError('неверный индекс клетки')

# game = TicTacToe()
# print(game.pole)
# game.clear()
# print(game.pole)
# game[0, 0] = 1
# game[1, 0] = 2
# print()
# # формируется поле:
# # 1 0 0
# # 2 0 0
# # 0 0 0
# # game[3, 2] = 2 # генерируется исключение IndexError
# if game[0, 0] == 0:
#     game[0, 0] = 2
# v1 = game[0, :]  # 1, 0, 0
# v2 = game[:, 0]  # 1, 2, 0
g = TicTacToe()
g.clear()
assert g[0, 0] == 0 and g[2, 2] == 0, "начальные значения всех клеток должны быть равны 0"
g[1, 1] = 1
g[2, 1] = 2
assert g[1, 1] == 1 and g[
    2, 1] == 2, "неверно отработала операция присваивания новых значений клеткам игрового поля (или, некорректно работает считывание значений)"

try:
    res = g[3, 0]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при считывании из несуществующей ячейки"

try:
    g[3, 0] = 5
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError при записи в несуществующую ячейку"

g.clear()
g[0, 0] = 1
g[1, 0] = 2
g[2, 0] = 3

assert g[0, :] == (1, 0, 0) and g[1, :] == (2, 0, 0) and g[:, 0] == (
1, 2, 3), "некорректно отработали срезы после вызова метода clear() и присваивания новых значений"

cell = Cell()
assert cell.value == 0, "начальное значение атрибута value класса Cell должно быть равно 0"
res = cell.is_free
cell.is_free = True
assert bool(cell), "функция bool вернула False для свободной клетки"