from typing import Union


class Dimensions:

    def __init__(self, a: Union[int, float], b: Union[int, float], c: Union[int, float]):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("габаритные размеры должны быть положительными числами")
        self.a = a
        self.b = b
        self.c = c

    def __hash__(self):
        return hash((self.a, self.b, self.c))

    def __eq__(self, other: "Dimensions"):
        return hash(self) == hash(other)



s_inp = "1 2 3; 4 5 6.78; 1 2 3; 3 1 2.5"

lst_dims = []
for s in s_inp.split('; '):
    a, b, c, = s.split()
    lst_dims.append(Dimensions(float(a), float(b), float(c)))
lst_dims.sort(key=hash)

