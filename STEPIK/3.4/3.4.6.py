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

    def push_back(self, obj: "StackObj") -> None:
        if not self.top:
            self.top = obj
        else:
            n = self.top
            while n.next is not None:
                n = n.next
            n.next = obj

    def pop_back(self):
        if self.top and self.top.next is None:
            self.top = None
        else:
            n = self.top
            while n.next is not None:
                if n.next.next is None:
                    n.next = None
                else:
                    n = n.next

    def __add__(self, add_obj: "StackObj") -> "Self":
        self.push_back(add_obj)
        return self

    # def __iadd__(self, add_obj: "StackObj") -> "Self":
    #     self.push_back(add_obj)
    #     return self

    def __mul__(self, lst_of_str_data) -> "Self":
        for string_obj in lst_of_str_data:
            self.push_back(StackObj(string_obj))
        return self

    # def __imul__(self, lst_of_str_data) -> "Self":
    #     for string_obj in lst_of_str_data:
    #         self.push_back(StackObj(string_obj))
    #     return self


assert hasattr(Stack, 'pop_back'), "класс Stack должен иметь метод pop_back"

st = Stack()
top = StackObj("1")
st.push_back(top)
assert st.top == top, "неверное значение атрибута top"

st = st + StackObj("2")
st = st + StackObj("3")
obj = StackObj("4")
st += obj

st = st * ['data_1', 'data_2']
st *= ['data_3', 'data_4']

d = ["1", "2", "3", "4", 'data_1', 'data_2', 'data_3', 'data_4']
h = top
i = 0
while h:
    assert h._StackObj__data == d[
        i], "неверное значение атрибута __data, возможно, некорректно работают операторы + и *"
    h = h._StackObj__next
    i += 1

assert i == len(d), "неверное число объектов в стеке"
