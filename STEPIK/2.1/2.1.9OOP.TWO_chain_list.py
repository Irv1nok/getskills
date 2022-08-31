class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj) -> None:
        if self.head:  # Если првый объект не создан.
            obj.set_prev(self.tail) # В объекте добавляем ссылку на предыдущий объект
            self.tail.set_next(obj) # В лок.атрб next последнего эл. доб ссылку на объект
            self.tail = obj # В лок. атрб. хвоста добавляем ссылку на объект
        else:
            self.head = obj
            self.tail = obj
        # if self.tail:  # Проверяем есть ли в лок.переменной данные
        #     self.tail.set_next(obj)  # Добавляем в next ссылку на след. объект класса
        #     obj.set_prev(self.tail)  # Добавляем в prev ссылку на предыдущий объект класс
        #     self.tail = obj
        #
        # if self.head and (self.head.get_next() is None):  # Создаем второй объект в связанном списке
        #     self.head.set_next(obj)  # Добавляем в next ссылку на след. объект класса
        #     obj.set_prev(self.head)  # Добавляем в prev ссылку на предыдущий объект класс
        #     self.tail = obj

    def remove_obj(self) -> None:
        # if self.head.get_next() is None:  # Проверка если это последний объект
        #     self.head = None
        #     self.tail = None
        if self.tail.get_prev():  # Если хвост существует
            self.tail = self.tail.get_prev()  # В перем. tail присваиваем ссылку на пред.объект
            self.tail.set_next(None)  # Ссылку на удаляемый объект удаляем
        else:
            self.head = None
            self.tail = None
        # if self.tail is self.head:  # Если первый объект и хвост совпадают
        #     self.tail = None

    def get_data(self) -> list:
        obj = self.head  # Ссылка на первый объект
        data = []
        while obj:  # Цикл по списку пока в next есть объект
            data.append(obj.get_data())  # Добавляем в список последний объект
            obj = obj.get_next()  # В obj присваивается объект что храниться в next
        return data


class ObjList:

    def __init__(self, data) -> None:
        self.__prev = None
        self.__data = data
        self.__next = None

    def set_next(self, obj) -> None:
        self.__next = obj

    def set_prev(self, obj) -> None:
        self.__prev = obj

    def get_next(self) :
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self, data) -> None:
        self.__data = data

    def get_data(self) -> str:
        return self.__data


lst = LinkedList()

lst.add_obj(ObjList("данные 1"))
lst.add_obj(ObjList("данные 2"))
lst.add_obj(ObjList("данные 3"))
res = lst.get_data()
print(res)
