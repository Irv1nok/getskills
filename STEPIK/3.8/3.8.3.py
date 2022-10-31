from typing import Union


class Track:

    def __init__(self, start_x: Union[int, float], start_y: Union[int, float]):
        self.start_x = start_x
        self.start_y = start_y
        self.point = []

    def add_point(self, x: Union[int, float], y: Union[int, float], speed: Union[int, float]) -> None:
        self.point.append([(x, y), speed])

    def chk_index(self, indx: int) -> None:
        if not type(indx) == int or not 0 <= indx <= (len(self.point) - 1):
            raise IndexError('некорректный индекс')

    def __getitem__(self, item: int) -> tuple:
        self.chk_index(item)
        return self.point[item]

    def __setitem__(self, key: int, value: Union[int, float]) -> None:
        self.chk_index(key)
        self.point[key][1] = value

tr = Track(10, -5.4)
tr.add_point(20, 0, 100) # первый линейный сегмент: indx = 0
tr.add_point(50, -20, 80) # второй линейный сегмент: indx = 1
tr.add_point(63.45, 1.24, 60.34) # третий линейный сегмент: indx = 2
print(tr[0])
print(tr[1])
print(tr[2])
tr[2] = 60
print(tr[2])
# c, s = tr[2]
# print(c, s)

# res = tr[3] # IndexError
