class ListInteger(list):

    def __init__(self, massive: list):
        super().__init__(massive)

    @staticmethod
    def check_massive(n: list):
        if type(n) == list:
            if any(map(lambda x: type(x) != int, n)):
                raise TypeError('можно передавать только целочисленные значения')
        elif type(n) != int:
            raise TypeError('можно передавать только целочисленные значения')
        else:
            pass

    def __setitem__(self, key, value):
        self.check_massive(value)
        super().__setitem__(key, value)

    def append(self, value):
        self.check_massive(value)
        super().append(value)


s = ListInteger((1, 2, 3))
print(s)
s[1] = 10
print(s)
s.append(11)
print(s)
s[0] = 10.5 # TypeError
