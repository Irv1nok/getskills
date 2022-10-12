from typing import Union



class ShopItem:

    def __init__(self, name: str, weight: Union[int, float], price: Union[int, float]) -> None:
        self.name = name
        self.weight = weight
        self.price = price

    def __eq__(self, other: "ShopItem"):
        return hash(self) == hash(other)

    def __hash__(self):
        return hash((self.name.lower(), self.weight, self.price))


lst_in = ['Системный блок: 1500 75890.56',
          'Монитор Samsung: 2000 34000',
          'Клавиатура: 200.44 545',
          'Монитор Samsung: 2000 34000']

# res = [[' '.join(x[:2]).rstrip(":"), float(x[2]), float(x[-1])] for x in list(map(lambda s: s.split(' '), lst_in))]
# ins = [ShopItem(*r) for r in res]
#
# total = Counter()
# shop_items = {}
# for items in ins:
#     total[items] += 1
#     shop_items[items] = [items, total[items]]
shop_items = {}

for s in lst_in:
    name, data = s.split(":")
    weight, price = data.split()
    obj = ShopItem(name, float(weight), float(price))
    shop_items.setdefault(obj, [obj, 0])[1] += 1

print(shop_items)
