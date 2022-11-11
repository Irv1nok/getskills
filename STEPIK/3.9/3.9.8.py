class StackObj:

    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None


class Stack:


    def __init__(self) -> None:
        self.top = None
        self.obj_count = 0

    def push_back(self, obj: "StackObj") -> None:
        if not self.top:
            self.top = obj
        else:
            n = self.top
            while n.next is not None:
                n = n.next
            n.next = obj
        self.obj_count += 1

    def push_front(self, obj: "StackObj"):
        obj.next = self.top
        self.top = obj

        self.obj_count += 1

    def check_indx(self, item: int):
        if type(item) != int or not 0 <= item <= self.obj_count - 1:
            raise IndexError('неверный индекс')

    def __getitem__(self, key: int, return_obj=False):
        self.check_indx(key)
        n = self.top
        count = 0
        while count != key:
            n = n.next
            count += 1

        return n.data if not return_obj else n

    def __setitem__(self, key: int, value: "StackObj"):
        self.check_indx(key)
        obj = self.__getitem__(key, return_obj=True)
        obj.data = value

    def __len__(self):
        return self.obj_count

    def __iter__(self):
        for i in range(self.obj_count):
            yield self.__getitem__(i, return_obj=True)


st = Stack()
st.push_back(StackObj("1"))
st.push_front(StackObj("2"))

assert st[0] == "2" and st[1] == "1", "неверные значения данных из объектов стека, при обращении к ним по индексу"

st[0] = "0"
print(st[0])
assert st[0] == "0", "получено неверное значение из объекта стека, возможно, некорректно работает присваивание нового значения объекту стека"

for obj in st:
    assert isinstance(obj, StackObj), "при переборе стека через цикл должны возвращаться объекты класса StackObj"

try:
    a = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"












###################################################################
    # def __setitem__(self, indx: int, new_obj: StackObj):
    #     if indx:  # if indx > 0 we sholud set new refrence for prev.obj.next and new_obj.next
    #         new_obj.next = self[indx].next  # new_obj.next = replaceable_obj.next
    #         self[indx - 1].next = new_obj  # previous_obj.next = new_obj
    #     else:
    #         new_obj.next = self.top.next
    #         self.top = new_obj
###################################################################