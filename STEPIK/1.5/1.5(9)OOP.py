class ListObject:
    """ОДНОСВЯЗНЫЙ СПИСОК"""

    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        end = ListObject(obj)
        n = self
        while n.next_obj:
            n = n.next_obj
        n.next_obj = end

lst_in = ['1111', '2222', '3333', '4444']
head_obj = ListObject(lst_in[0])
for i in range(1, len(lst_in)):
    head_obj.link(lst_in[i])

"""Вывод информации с односвязного списка"""
# node = head_obj
# print(node.data)
# while node.next_obj:
#     node = node.next_obj
#     print(node.data)