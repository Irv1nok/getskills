from math import sqrt


class RadiusVector:

    def __init__(self, *args):
        self.vector = args
        self.r_vector = len(self.vector)

    @property
    def vector(self):
        return self.__vector

    @vector.setter
    def vector(self, numbers):
        if all(isinstance(num, (int, float)) for num in numbers):
            if len(numbers) > 1:
                self.__vector = list(numbers)
            else:
                if type(*numbers) == int:
                    self.__vector = [0 for i in range(*numbers)]

    def set_coords(self, *args):
        for i, num in enumerate(args):
            if i < self.r_vector:
                self.vector[i] = num

    def get_coords(self):
        return tuple(self.vector)

    def __len__(self):
        return len(self.vector)

    def __abs__(self):
        result = sqrt(sum([n**2 for n in self.vector]))
        return result


vector3D = RadiusVector(10, 20, 30, 40)
# vector3D.set_coords(10, 20, 30, 40)
a, b, c, d = vector3D.get_coords()
vector3D.set_coords(3, -5.6, 8, 10, 11)  # ошибки быть не должно, последние две координаты игнорируются
vector3D.set_coords(1, 2) # ошибки быть не должно, меняются только первые две координаты

res_len = len(vector3D) # res_len = 3
res_abs = abs(vector3D)
print(res_abs)
print(vector3D.__dict__)
