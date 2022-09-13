from typing import Union


class NewList:

    def __init__(self, list_elements: list = None) -> None:
        self.list_elements = list_elements.copy() if list_elements and type(list_elements) == list else []

    def get_list(self):
        return self.list_elements

    def sub_func_list(self, list_1: Union["NewList", list], list_2: Union["NewList", list]) -> "NewList":
        sub = list_2.copy()
        res = []
        for j in list_1:
            if any(map(lambda x: type(j) == type(x) and j == x, sub)):
                sub.remove(j)
            else:
                res.append(j)
        return res

    def __sub__(self, other):
        if not isinstance(other, (list, NewList)):
            raise ArithmeticError("Правый операнд должен быть int или float или NewList")

        inst_or_num = other if type(other) == list else other.get_list()
        return NewList(self.sub_func_list(self.get_list(), inst_or_num))

    def __rsub__(self, other):
        return NewList(self.sub_func_list(other, self.get_list()))



lst = NewList()
lst1 = NewList([0, 1, -3.4, "abc", True])
lst2 = NewList([1, 0, True])

assert lst1.get_list() == [0, 1, -3.4, "abc", True] and lst.get_list() == [], "метод get_list вернул неверный список"

res1 = lst1 - lst2
res2 = lst1 - [0, True]
res3 = [1, 2, 3, 4.5] - lst2

lst1 -= lst2

assert res1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"
assert res2.get_list() == [1, -3.4, "abc"], "метод get_list вернул неверный список"
assert res3.get_list() == [2, 3, 4.5], "метод get_list вернул неверный список"
assert lst1.get_list() == [-3.4, "abc"], "метод get_list вернул неверный список"

lst_1 = NewList([1, 0, True, False, 5.0, True, 1, True, -7.87])
lst_2 = NewList([10, True, False, True, 1, 7.87])
res = lst_1 - lst_2
assert res.get_list() == [0, 5.0, 1, True, -7.87], "метод get_list вернул неверный список"

a = NewList([2, 3])
res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
assert res_4.get_list() == [1, 2], "метод get_list вернул неверный список"
# lst1 = NewList([1, 2, -4, 6, 10, 11, 15, False, True])
# lst2 = NewList([0, 1, 2, 3, True])
# res_1 = lst1 - lst2  # NewList: [-4, 6, 10, 11, 15, False]
# print(res_1.get_list())
# lst1 -= lst2  # NewList: [-4, 6, 10, 11, 15, False]
# print(lst1.get_list())
# res_2 = lst2 - [0, True]  # NewList: [1, 2, 3]
# print(res_2.get_list())
# res_3 = [1, 2, 3, 4.5] - res_2 # NewList: [4.5]
# print(res_3.get_list())
# a = NewList([2, 3])
# res_4 = [1, 2, 2, 3] - a # NewList: [1, 2]
# print(res_4.get_list())
