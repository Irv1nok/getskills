from typing import Union


class Box3D:

    def __init__(self, width: Union[int, float], height: Union[int, float], depth: Union[int, float]) -> None:
        self.width = width
        self.height = height
        self.depth = depth

    def __add__(self, other: "Box3D") -> "Box3D":
        res = list(map(lambda x, y: x + y, self.__dict__.values(), other.__dict__.values()))
        return Box3D(*res)

    def __sub__(self, other: "Box3D") -> "Box3D":
        res = list(map(lambda x, y: x - y, self.__dict__.values(), other.__dict__.values()))
        return Box3D(*res)

    def __mul__(self, other: "Box3D") -> "Box3D":
        res = list(map(lambda x: x * other, self.__dict__.values()))
        return Box3D(*res)

    def __rmul__(self, other: int) -> "Box3D":
        res = list(map(lambda x: x * other, self.__dict__.values()))
        return Box3D(*res)

    def __floordiv__(self, other: int) -> "Box3D":
        res = list(map(lambda x: x // other, self.__dict__.values()))
        return Box3D(*res)

    def __mod__(self, other: int) -> "Box3D":
        res = list(map(lambda x: x % other, self.__dict__.values()))
        return Box3D(*res)


box1 = Box3D(1, 2, 3)

box2 = Box3D(2, 4, 6)

# box = box1 + box2
# print(box.__dict__)
# boxx = box2 - box1
# print(boxx.__dict__)
# box = box1 * 1
# bbox = 3 * box2
# box = box1 // 2
box = box2 % 3

print(box.__dict__)
