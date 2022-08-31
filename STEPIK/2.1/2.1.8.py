class Point:

    def __init__(self, x: int, y: int) -> None:
        self.__x = x
        self.__y = y

    def get_coords(self) -> tuple:
        return self.__x, self.__y


class Rectangle:

    def __init__(self, *args) -> None:
        if len(args) == 4:
            x1, y1, x2, y2 = args
            self.set_coords(Point(x1, y1), Point(x2, y2))
        elif len(args) == 2:
            self.set_coords(*args)
        else:
            raise ValueError('Wrong arguments')

    def set_coords(self, sp: Point, ep: Point) -> None:
        self.__sp = sp
        self.__ep = ep

    def get_coords(self) -> tuple:
        return self.__sp, self.__ep

    def draw(self) -> str:
        print(f'Прямоугольник с координатами: {self.__sp.get_coords()} {self.__ep.get_coords()}') # Вызывает ф. get_coords класс Point

r1 = Rectangle(Point(1, 2), Point(3, 4))
r1.draw()
# rect = Rectangle(0, 0, 20, 34)
# rect.draw()