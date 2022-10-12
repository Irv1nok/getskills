from typing import Union


class Ellipse:

    def __init__(self, *args: Union[int, float]):
        if args:
            try:
                self.x1, self.y1, self.x2, self.y2 = args
            except ValueError:
                print(f'class {type(self).__name__} need four arguments!')

    def __bool__(self) -> bool:
        return bool(self.__dict__)

    def get_coords(self) -> tuple:
        if not bool(self):
            raise AttributeError('нет координат для извлечения')
        return self.x1, self.y1, self.x2, self.y2


lst_geom = [Ellipse(), Ellipse(), Ellipse(1, 2, 3, 4), Ellipse(5, 6, 7, 8)]
for l in lst_geom:
    if bool(l):
        l.get_coords()