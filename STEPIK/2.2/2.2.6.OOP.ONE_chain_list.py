class StackObj:

    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) == StackObj or obj is None:
            self.__next = obj

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, arg):
        self.__data = arg


class Stack:

    def __init__(self):
        self.top = None

    def push(self, obj):
        if not self.top:
            self.top = obj
        else:
            first = self.top
            while first.next:
                first = first.next
            first.next = obj

    def pop(self):
        if not self.top.next:
            self.top = None
        else:
            obj = self.top
            prev = None
            while obj.next: #while current.next.next is not None: В ссылке на объект вызывается метод next.
                prev = obj  #current = current.next
                obj = obj.next  #current.next = None
            prev.next = None

    def get_data(self):
        obj = self.top
        data = []
        while obj != None:
            data.append(obj.data)
            obj = obj.next
        return data


# st = Stack()
# st.push(StackObj("obj1"))
# st.push(StackObj("obj2"))
# st.push(StackObj("obj3"))
s = Stack()
top = StackObj("obj_1")
s.push(top)
s.push(StackObj("obj_2"))
s.push(StackObj("obj_3"))
s.pop()

res = s.get_data()
assert res == ["obj_1", "obj_2"], f"метод get_data вернул неверные данные: {res}"
assert s.top == top, "атрибут top объекта класса Stack содержит неверное значение"

h = s.top
while h:
    res = h.data
    h = h.next

s = Stack()
top = StackObj("obj_1")
s.push(top)
s.pop()
assert s.get_data() == [], f"метод get_data вернул неверные данные: {s.get_data()}"

n = 0
h = s.top
while h:
    h = h.next
    n += 1