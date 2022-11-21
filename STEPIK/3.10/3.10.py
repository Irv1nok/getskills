from random import randint


class Cell:

    def __init__(self):
        self.value = 0

    def __bool__(self):
        return True if self.value == 0 else False

    def __repr__(self):
        return "*" if self.value == 0 else 'X' if self.value == 1 else '0'


class TicTacToe:
    FREE_CELL = 0  # свободная клетка
    HUMAN_X = 1  # крестик (игрок - человек)
    COMPUTER_O = 2  # нолик (игрок - компьютер)

    def __init__(self):
        self.pole = [[Cell() for _ in range(3)] for _ in range(3)]
        self.turn = 0

    def check_indx(self, indx):
        for i in indx:
            if type(i) != int or not 0 <= i <= 2:
                raise IndexError('некорректно указанные индексы')

    def __getitem__(self, key):
        self.check_indx(key)
        i, j = key
        return self.pole[i][j].value

    def __setitem__(self, key, value):
        self.check_indx(key)
        i, j = key
        if self.pole[i][j].value != 0:
            print('Введите свободную клетку!')
            self.human_go()
        self.pole[i][j].value = value
        self.turn += 1

    def init(self):
        self.__init__()

    def show(self):
        for x in self.pole:
            print(x)

    def human_go(self):
        i, j = input("Введите координаты клетки через пробел: ").split()
        self.__setitem__((int(i), int(j)), 1)

    def randomize(self):
        i = randint(0, 2)
        j = randint(0, 2)
        return i, j

    def computer_go(self):
        i, j = self.randomize()
        if self.pole[i][j].value == 0:
            self.pole[i][j].value = 2
            self.turn += 1
            print('Computer turn >')
        else:
            self.computer_go()

    def check_pole(self, hum_or_comp):
        res = hum_or_comp
        for i in range(3):
            if self.pole[i][0].value == res and self.pole[i][1].value == res and self.pole[i][2].value == res:
                return True

        for j in range(3):
            if self.pole[0][j].value == res and self.pole[1][j].value == res and self.pole[2][j].value == res:
                return True

        if self.pole[0][0].value == res and self.pole[1][1].value == res and self.pole[2][2].value == res:
            return True

        if self.pole[0][2].value == res and self.pole[1][1].value == res and self.pole[2][0].value == res:
            return True

        return False

    @property
    def is_human_win(self):
        return self.check_pole(1)

    @property
    def is_computer_win(self):
        return self.check_pole(2)

    @property
    def is_draw(self):
        if self.turn == 9 and not self.is_human_win and not self.is_computer_win:
            return True
        else:
            return False

    def __bool__(self):
        if self.turn < 9 and not self.is_human_win and not self.is_computer_win:
            return True
        else:
            return False


game = TicTacToe()
game.init()
step_game = 0
while game:
    game.show()

    if step_game % 2 == 0:
        game.human_go()
    else:
        game.computer_go()

    step_game += 1


game.show()

if game.is_human_win:
    print("Поздравляем! Вы победили!")
elif game.is_computer_win:
    print("Все получится, со временем")
else:
    print("Ничья.")


# cell = Cell()
# assert cell.value == 0, "начальное значение атрибута value объекта класса Cell должно быть равно 0"
# assert bool(cell), "функция bool для объекта класса Cell вернула неверное значение"
# cell.value = 1
# assert bool(cell) == False, "функция bool для объекта класса Cell вернула неверное значение"
#
# assert hasattr(TicTacToe, 'show') and hasattr(TicTacToe, 'human_go') and hasattr(TicTacToe, 'computer_go'), "класс TicTacToe должен иметь методы show, human_go, computer_go"
#
# game = TicTacToe()
# assert bool(game), "функция bool вернула неверное значения для объекта класса TicTacToe"
# assert game[0, 0] == 0 and game[2, 2] == 0, "неверные значения ячеек, взятые по индексам"
# game[1, 1] = TicTacToe.HUMAN_X
# assert game[1, 1] == TicTacToe.HUMAN_X, "неверно работает оператор присваивания нового значения в ячейку игрового поля"
#
# game[0, 0] = TicTacToe.COMPUTER_O
# assert game[0, 0] == TicTacToe.COMPUTER_O, "неверно работает оператор присваивания нового значения в ячейку игрового поля"
#
# game.init()
# assert game[0, 0] == TicTacToe.FREE_CELL and game[1, 1] == TicTacToe.FREE_CELL, "при инициализации игрового поля все клетки должны принимать значение из атрибута FREE_CELL"
#
# try:
#     game[3, 0] = 4
# except IndexError:
#     assert True
# else:
#     assert False, "не сгенерировалось исключение IndexError"
#
# game.init()
#
# assert game.is_human_win == False and game.is_computer_win == False and game.is_draw == False, "при инициализации игры атрибуты is_human_win, is_computer_win, is_draw должны быть равны False, возможно не пересчитывается статус игры при вызове метода init()"
#
# game[0, 0] = TicTacToe.HUMAN_X
# game[1, 1] = TicTacToe.HUMAN_X
# game[2, 2] = TicTacToe.HUMAN_X
# assert game.is_human_win and game.is_computer_win == False and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"
#
# game.init()
# game[0, 0] = TicTacToe.COMPUTER_O
# game[1, 0] = TicTacToe.COMPUTER_O
# game[2, 0] = TicTacToe.COMPUTER_O
# assert game.is_human_win == False and game.is_computer_win and game.is_draw == False, "некорректно пересчитываются атрибуты is_human_win, is_computer_win, is_draw. Возможно не пересчитывается статус игры в момент присвоения новых значения по индексам: game[i, j] = value"