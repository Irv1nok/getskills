from random import randint, choice

"""Представления клетки игрового поля"""


class Cell:

    def __init__(self, around_mines: int, mine: bool):
        self.around_mines = around_mines  # число мин вокруг данной клетки поля
        self.mine = mine  # наличие мины в текущей клетке
        self.fl_open = False  # открыта/закрыта клетка


"""Управление игровым полем, размером N x N клеток"""


class GamePole:
    count_mines = 0

    def __init__(self, N: int, M: int):
        self.N = N  # размер поля
        self.M = M  # общее число мин на поле
        self.pole = [[] for i in range(N)]  # хранятся в двумерном списке N x N элементов
        self.init()  # первоначальная инициализация игрового поля

    """Генератор мин"""

    def rand_mine(self):
        if GamePole.count_mines == self.M:
            return False
        if choice([False, False, True, False, False]):  # генератор криво работает, поле не полностью
            GamePole.count_mines += 1                          # заполено, увел.число False
            return True
        else:
            return False

    """Инициализация поля с  расстановкой М мин"""

    def init(self):
        for x in range(self.N):  # создание поля
            for y in range(self.N):
                self.pole[x].append(Cell(0, self.rand_mine()))

        # if GamePole.count_mines != self.M:  # проверяем все ли мины расставлены
        #     self.init()

        for x in range(self.N):
            for y in range(self.N):

                # Пропускаем если мина в клетке
                if self.pole[x][y].mine:
                    continue

                # Проверяем верх
                if x > 0 and self.pole[x - 1][y].mine:
                    self.pole[x][y].around_mines = self.pole[x][y].around_mines + 1
                # Проверяем низ
                if x < self.N - 1 and self.pole[x + 1][y].mine:
                    self.pole[x][y].around_mines = self.pole[x][y].around_mines + 1
                # Лево
                if y > 0 and self.pole[x][y - 1].mine:
                    self.pole[x][y].around_mines = self.pole[x][y].around_mines + 1
                # Право
                if y < self.N - 1 and self.pole[x][y + 1].mine:
                    self.pole[x][y].around_mines = self.pole[x][y].around_mines + 1
                # Верх-лево
                if x > 0 and y > 0 and self.pole[x - 1][y - 1].mine:
                    self.pole[x][y].around_mines = self.pole[x][y].around_mines + 1
                # Верх-право
                if x > 0 and y < self.N - 1 and self.pole[x - 1][y + 1].mine:
                    self.pole[x][y].around_mines = self.pole[x][y].around_mines + 1
                # Лево-низ
                if x < self.N - 1 and y > 0 and self.pole[x + 1][y - 1].mine:
                    self.pole[x][y].around_mines = self.pole[x][y].around_mines + 1
                # Право-низ
                if x < self.N - 1 and y < self.N - 1 and self.pole[x + 1][y + 1].mine:
                    self.pole[x][y].around_mines = self.pole[x][y].around_mines + 1


    """Отображение поля в консоли в виде таблицы чисел открытых клеток"""

    def show_sharps(self):
        for x in range(self.N):
            for y in range(self.N):
                if not self.pole[x][y].fl_open:
                    print(f'#', end=' ')
                else:
                    print(f'{self.pole[x][y].around_mines}', end=' ')
            print()

    def show(self):
        for x in range(self.N):
            for y in range(self.N):
                if self.pole[x][y].mine:
                    print(f'*', end=' ')
                else:
                    print(f'{self.pole[x][y].around_mines}', end=' ')
            print()

if __name__ == '__main__':

    pole_game = GamePole(10, 12)
    pole_game.show()
