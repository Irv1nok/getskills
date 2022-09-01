class LinkedList:

    def __init__(self) ->None:
        self.head = None
        self.tail = None

    def add_obj(self, obj):
        if not self.head:
            self.head = obj
            self.tail = obj
        else:
            self.tail.next = obj
            obj.prev = self.tail
            self.tail = obj

    def remove_obj(self, indx):
        ...

    def __len__(self):
        if self.head:
            count = 1
            n = self.head
        else:
            return 0
        while n.next != None:
            n = n.next
            count += 1
        return count

    def __call__(self, indx, *args, **kwargs):
        return self[indx]


class ObjList:

    def __init__(self, data):
        self.__data = data
        self.__prev = None
        self.__next = None

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, obj):
        self.__prev = obj

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        self.__next = obj


linked_lst = LinkedList()
linked_lst.add_obj(ObjList("Sergey"))
linked_lst.add_obj(ObjList("Balakirev"))
linked_lst.add_obj(ObjList("Python"))
print(linked_lst.__dict__)
# linked_lst.remove_obj(2)
# linked_lst.add_obj(ObjList("Python ООП"))
n = len(linked_lst)  # n = 3
print(n)
# s = linked_lst(1) # s = Balakirev