class Tuple(tuple):

    def __add__(self, iterable):
        return Tuple(super().__add__(tuple(iterable)))


t = Tuple([1, 2, 3])
t = t + "Python"

