# from functools import wraps
# from random import randint
class NewList(list):

    def __sub__(self, other: ('NewList', 'list')) -> 'NewList':
        tmp_lst = [(i, type(i)) for i in self]
        for i in [(i, type(i)) for i in other]:
            if i in tmp_lst:
                tmp_lst.remove(i)
        return NewList(i[0] for i in tmp_lst)

    def __rsub__(self, other):
        return NewList(other) - self

    def get_list(self):
        return self


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

# new_list_elements = self.list_elements.copy()
#
#         for i, j in enumerate(self.list_elements):
#             for k in inst_or_num:
#                 if type(j) == bool and type(k) == bool:
#                     if j == k:
#                         el new_list_elements[i]


# a = 5400
# h = (a // 3600)
# m = (a % 3600 // 60)
# s = (a % 3600 % 60)
# print(f'{h:02}: {m:02}: {s:02}')
#
#
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print("Do something")
#         res = func(*args, **kwargs)
#         print(("end something"))
#         return res
#
#     return wrapper
#
#
# @decorator
# def sum_two_int(x, y):
#     return x + y
#
#
# sum_two_int = decorator(sum_two_int)
#
# list_obj = [randint(1, 20) for _ in range(10)]
# print(list_obj)
#
# for x in range(len(list_obj) - 1):
#     for y in range(x + 1, len(list_obj)):
#         if list_obj[x] > list_obj[y]:
#             list_obj[x], list_obj[y] = list_obj[y], list_obj[x]
#
# print(list_obj)
