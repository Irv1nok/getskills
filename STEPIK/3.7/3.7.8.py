from random import randint


class GamePole:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, n: int, m: int, total_mines: int):
        self.n = n
        self.m = m
        self.total_mines = total_mines
        self.__pole_cells = [[Cell() for n in range(self.m)] for n in range(self.n)]

    @property
    def pole(self):
        return self.__pole_cells

    def init_pole(self):
        mines = 0
        while mines < self.total_mines:
            i = randint(0, self.n - 1)
            j = randint(0, self.m - 1)
            if self.pole[i][j].is_mine:
                continue
            self.pole[i][j].is_mine = True
            mines += 1

        indx = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
        for x in range(self.n):
            for y in range(self.m):
                if not self.pole[x][y].is_mine:
                    around_mine = sum((self.pole[x + i][y + j].is_mine for i, j in indx if
                                       0 <= x + i < self.n and 0 <= y + j < self.m))
                    self.pole[x][y].number = around_mine

    def open_cell(self, i, j):
        if not 0 <= i <= (self.n - 1) or not 0 <= j <= (self.m - 1):
            raise IndexError('некорректные индексы i, j клетки игрового поля')
        self.__pole_cells[i][j].is_open = True

    def show_pole(self):
        for i in self.pole:
            for j in i:
                print('#' if not j.is_open else j.number if not j.is_mine else '*', end=' ')
            print()
        print()


class Cell:

    def __init__(self):
        self.__is_mine: bool = False
        self.__number: int = 0
        self.__is_open: bool = False

    @property
    def is_mine(self) -> bool:
        return self.__is_mine

    @is_mine.setter
    def is_mine(self, b: bool) -> None:
        if type(b) != bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_mine = b

    @property
    def number(self) -> int:
        return self.__number

    @number.setter
    def number(self, n: int) -> None:
        if not type(n) == int or not 0 <= n <= 8:
            raise ValueError("недопустимое значение атрибута")
        self.__number = n

    @property
    def is_open(self) -> bool:
        return self.__is_open

    @is_open.setter
    def is_open(self, b: bool):
        if not type(b) == bool:
            raise ValueError("недопустимое значение атрибута")
        self.__is_open = b

    def __bool__(self) -> bool:
        if not self.is_open:
            return True
        else:
            return False

pole = GamePole(10, 20, 10)  # создается поле размерами 10x20 с общим числом мин 10
pole.init_pole()
if pole.pole[0][1]:
    pole.open_cell(0, 1)
if pole.pole[3][5]:
    pole.open_cell(3, 5)
# pole.open_cell(30, 100)  # генерируется исключение IndexError
pole.show_pole()
# p1 = GamePole(10, 20, 10)
# p2 = GamePole(10, 20, 10)
# assert id(p1) == id(p2), "создается несколько объектов класса GamePole"
# p = p1
#
# cell = Cell()
# assert type(Cell.is_mine) == property and type(Cell.number) == property and type(
#     Cell.is_open) == property, "в классе Cell должны быть объекты-свойства is_mine, number, is_open"
#
# cell.is_mine = True
# cell.number = 5
# cell.is_open = True
#
# assert bool(cell) == False, "функция bool() вернула неверное значение"
#
# try:
#     cell.is_mine = 10
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# try:
#     cell.number = 10
# except ValueError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение ValueError"
#
# p.init_pole()
# m = 0
# for row in p.pole:
#     for x in row:
#         assert isinstance(x, Cell), "клетками игрового поля должны быть объекты класса Cell"
#         if x.is_mine:
#             m += 1
#
# assert m == 10, "на поле расставлено неверное количество мин"
# p.open_cell(0, 1)
# p.open_cell(9, 19)
#
# try:
#     p.open_cell(10, 20)
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
#
#
# def count_mines(pole, i, j):
#     n = 0
#     for k in range(-1, 2):
#         for l in range(-1, 2):
#             ii, jj = k + i, l + j
#             if ii < 0 or ii > 9 or jj < 0 or jj > 19:
#                 continue
#             if pole[ii][jj].is_mine:
#                 n += 1
#
#     return n
#
#
# for i, row in enumerate(p.pole):
#     for j, x in enumerate(row):
#         if not p.pole[i][j].is_mine:
#             m = count_mines(p.pole, i, j)
#             assert m == p.pole[i][j].number, "неверно подсчитано число мин вокруг клетки"
