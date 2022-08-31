# class Money:
#
#     def __init__(self, money: int):
#         self.__money = money
#
#     def set_money(self, money):
#         if self.check_money(money):
#             self.__money = money
#
#     def get_money(self):
#         return self.__money
#
#     def add_money(self, mn):
#         self.set_money(mn.get_money() + self.get_money())
#
#     @classmethod
#     def check_money(cls, money):
#         return isinstance(money, int) and money >= 0
#
# mn_1 = Money(10)
# mn_2 = Money(20)
# mn_1.set_money(100)
# mn_2.add_money(mn_1)
# m1 = mn_1.get_money()  # 100
# m2 = mn_2.get_money()  # 120
# print(m1)
# print(m2)
























# class Clock:
#
#     def __init__(self, time=0):
#         self.__time = time
#
#     def set_time(self, tm):
#         if self.check_time(tm):
#             self.__time = tm
#
#
#     def get_time(self):
#         return self.__time
#
#     def check_time(self, tm):
#         if isinstance(tm, int) and 0 <= tm < 100_000:
#             return True
#         return False
#
#
# clock = Clock(4530)
# clock.set_time(1)