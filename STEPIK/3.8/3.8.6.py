from typing import Union


class StackObj:

    def __init__(self, data: str) -> None:
        self.data = data
        self.next = None

    @property
    def data(self) -> str:
        return self.__data

    @data.setter
    def data(self, data_string: str):
        if type(data_string) == str:
            self.__data = data_string

    @property
    def next(self) -> Union[None, "StackObj"]:
        return self.__next

    @next.setter
    def next(self, add_obj: "StackObj"):
        if isinstance(add_obj, StackObj) or add_obj is None:
            self.__next = add_obj


class Stack:

    def __init__(self) -> None:
        self.top = None
        self.obj_count = 0

    def push(self, obj: "StackObj") -> None:
        if not self.top:
            self.top = obj
        else:
            n = self.top
            while n.next is not None:
                n = n.next
            n.next = obj
        self.obj_count += 1

    def pop(self):
        if self.top and self.top.next is None:
            self.top = None
            self.obj_count = 0
            return self.top
        else:
            n = self.top
            while n.next is not None:
                if n.next.next is None:
                    res = n.next
                    n.next = None
                    return res
                else:
                    n = n.next
        self.obj_count -= 1

    def __getitem__(self, item):
        if type(item) != int or not 0 <= item <= self.obj_count - 1:
            raise IndexError('неверный индекс')

        n = self.top
        count = 0
        while count != item:
            n = n.next
            count += 1
        return n
###################################################################
    # def __setitem__(self, indx: int, new_obj: StackObj):
    #     if indx:  # if indx > 0 we sholud set new refrence for prev.obj.next and new_obj.next
    #         new_obj.next = self[indx].next  # new_obj.next = replaceable_obj.next
    #         self[indx - 1].next = new_obj  # previous_obj.next = new_obj
    #     else:
    #         new_obj.next = self.top.next
    #         self.top = new_obj
###################################################################
    def __setitem__(self, key, value):
        if type(key) != int or not 0 <= key <= self.obj_count:
            raise IndexError('неверный индекс')
        print(self.__dict__)
        print(self[1])
        n = self.top
        count = 0
        while count != key:
            count += 1
            if count == key:
                obj = n.next.next
                n.next = value
                n.next.next = obj
                break
            n = n.next


st = Stack()
st.push(StackObj("obj11"))
st.push(StackObj("obj12"))
st.push(StackObj("obj13"))
st[1] = StackObj("obj2-new")
assert st[0].data == "obj11" and st[
    1].data == "obj2-new", "атрибут data объекта класса StackObj содержит неверные данные"

try:
    obj = st[3]
except IndexError:
    assert True
else:
    assert False, "не сгенерировалось исключение IndexError"

obj = st.pop()
assert obj.data == "obj13", "метод pop должен удалять последний объект стека и возвращать его"

n = 0
h = st.top
while h:
    assert isinstance(h, StackObj), "объект стека должен быть экземпляром класса StackObj"
    n += 1
    h = h.next

assert n == 2, "неверное число объектов в стеке (возможно, нарушена его структура)"