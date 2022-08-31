class Translator:

    lst = []

    def add(self, eng, rus):
        self.lst.append([eng, rus])

    def remove(self, eng):
        for i in self.lst:
            if i[0] == eng:
                i.pop

    def translate(self, eng):
        return [i[1] for i in self.lst if i[0] == eng]

tr = Translator()
tr.add("car", "машина")
tr.add("tree", "дерево")
tr.add("car", "автомобиль")
tr.add("leaf", "лист")
tr.add("river", "река")
tr.add("go", "идти")
tr.add("go", "ехать")
tr.add("go", "ходить")
tr.add("milk", "молоко")
tr.remove('car')
print(*tr.translate("go"))

# from typing import List, Dict
#
#
# class Translator:
#     dictionary: Dict[str, List[str]]
#
#     def __init__(self):
#         self.dictionary = {}
#
#     def add(self, eng: str, rus: str) -> None:
#         if eng not in self.dictionary:
#             self.dictionary[eng] = []
#         self.dictionary[eng].append(rus)
#
#     def remove(self, eng: str) -> None:
#         self.dictionary.pop(eng)
#
#     def translate(self, eng: str) -> List[str]:
#         return self.dictionary[eng]
#
#
# tr = Translator()
#
# for pair_of_words in ('tree - дерево', 'car - машина', 'car - автомобиль',
#                       'leaf - лист', 'river - река', 'go - идти',
#                       'go - ехать', 'go - ходить', 'milk - молоко'):
#     tr.add(*pair_of_words.split(' - '))
#
# tr.remove('car')
#
# print(*tr.translate('go'))

