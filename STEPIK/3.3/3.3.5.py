class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def add_obj(self, obj: 'ObjList'):
        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx: int):
        res = self.pass_link_list(indx=indx)
        if res.next:
            if res.prev:
                res.prev.next = res.next
                res.next.prev = res.prev
                del res
            else:
                res.next.prev = res.prev
                self.head = res.next
                del res
        elif res == self.head:
            self.head = None
            self.tail = None

        else:
            self.tail = res.prev
            res.prev.next = None
            del res

    def pass_link_list(self, indx: int = None):
        if self.head:
            count = 0
            obj = self.head
        else:
            return None

        while obj is not None:
            if count == indx:
                return obj

            obj = obj.next
            count += 1
        return count

    def __len__(self):
        return self.pass_link_list()

    def __call__(self, indx, *args, **kwargs):
        res = self.pass_link_list(indx=indx)
        return res.data


class ObjList:

    def __init__(self, data: str) -> None:
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, string):
        if type(string) == str:
            self.__data = string

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        if type(obj) in (ObjList, None):
            self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if type(obj) in (ObjList, None):
            self.__next = obj


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
linked_lst.remove_obj(2)
linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
print(n)
s = linked_lst(1) # s = Balakirev