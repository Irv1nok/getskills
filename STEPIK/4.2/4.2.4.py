class Thing:

    def __init__(self, name: str, price: float, weight: float):
        self.name = name
        self.price = price
        self.weight = weight

    def __hash__(self):
        return hash((self.name, self.price, self.weight))


class DictShop(dict):

    def __init__(self, things=None):
        things = {} if things is None else things

        if not isinstance(things, dict):
            raise TypeError('аргумент должен быть словарем')
        self.check_keys(things)
        super().__init__(things)

    def check_keys(self, obj):
        if type(obj) == dict:
            for x in obj:
                if isinstance(x, Thing):
                    raise TypeError('ключами могут быть только объекты класса Thing')

        elif isinstance(obj, Thing):
            raise TypeError('ключами могут быть только объекты класса Thing')

    def __setitem__(self, key, value):
        self.check_keys(key)
        super().__setitem__(key, value)

th_1 = Thing('Лыжи', 11000, 1978.55)
th_2 = Thing('Книга', 1500, 256)
# d = {}
# d['val'] = 1

dict_things = DictShop()
# x = DictShop({t1: t1, t2: t2})
# print(x)
dict_things[th_1] = th_1
dict_things[th_2] = th_2
# for x in dict_things:
#     print(x)
#     print(x.name)