class Cart:

    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f"{i.name}: {i.price}" for i in self.goods]

class Table:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:

    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:

    def __init__(self, name, price):
        self.name = name
        self.price = price


lg = TV('LG', 23000)
samsung = TV('Samsung', 122300)
ikea = Table('IKEA', 3000)
macbook = Notebook('MacBook', 289000)
matebook = Notebook('MateBook', 102300)
coffe = Cup('Coffee', 230)

cart = Cart()
cart.add(lg)
cart.add(samsung)
cart.add(ikea)
cart.add(macbook)
cart.add(matebook)
print(cart.get_list())