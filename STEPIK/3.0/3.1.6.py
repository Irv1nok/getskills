class Validate:

    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        if type(value) == str:
            return setattr(instance, self.name, value)

        raise TypeError("Неверный тип присваиваемых данных")


class Museum:

    def __init__(self, name: str) -> None:
        self.name = name
        self.exhibits = []

    def add_exhibit(self, obj) -> None:
        self.exhibits.append(obj)

    def remove_exhibit(self, obj) -> None:
        if obj in self.exhibits:
            self.exhibits.remove(obj)

    def get_info_exhibit(self, indx):
        obj = self.exhibits[indx]
        return f'Описание экспоната {obj.name}: {obj.descr}'


class Picture:
    name = Validate()
    author = Validate()
    descr = Validate()

    def __init__(self, name: str, author: str, descr: str) -> None:
        self.name = name
        self.author = author
        self.descr = descr


class Mummies:
    name = Validate()
    location = Validate()
    descr = Validate()

    def __init__(self, name: str, location: str, descr: str) -> None:
        self.name = name
        self.location = location
        self.descr = descr


class Papyri:
    name = Validate()
    date = Validate()
    descr = Validate()

    def __init__(self, name: str, date: str, descr: str) -> None:
        self.name = name
        self.date = date
        self.descr = descr


# class Exhibit:
#
#     def __setattr__(self, key, value):
#         if not isinstance(value, str):
#             raise ValueError()
#         super().__setattr__(key, value)
#
#     def __repr__(self):
#         return f'Описание экспоната {self.name}: {self.descr}'

# class Picture(Exhibit):
#
#     def __init__(self, name, author, descr):
#         self.name = name
#         self.author = author
#         self.descr = descr
#
#
# class Mummies(Exhibit):
#
#     def __init__(self, name, loc, descr):
#         self.name = name
#         self.location = loc
#         self.descr = descr
#
#
# class Papyri(Exhibit):
#
#     def __init__(self, name, date, descr):
#         self.name = name
#         self.date = date
#         self.descr = descr
#
# class Museum:
#
#     def __init__(self, name):
#         self.name = name
#         self.exhibits = []
#
#     def add_exhibit(self, ex):
#         if isinstance(ex, Exhibit):
#             self.exhibits.append(ex)
#
#     def remove_exhibit(self, ex):
#         if ex in self.exhibits:
#             self.exhibits.remove(ex)
#
#     def get_info_exhibit(self, index):
#         if abs(index) <= len(self.exhibits) - 1:
#             return str(self.exhibits[index])
