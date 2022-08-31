class Course:

    def __init__(self, name: str) -> None:
        self.name = name
        self.modules = []

    def add_module(self, module: 'Module') -> None:
        self.modules.append(module)

    def remove_module(self, indx: int) -> None:
        self.modules.pop(indx)


class Module:

    def __init__(self, name: str) -> None:
        self.name = name
        self.lessons = []

    def add_lesson(self, lesson: 'LessonItem') -> None:
        self.lessons.append(lesson)

    def remove_lesson(self, indx: int) -> None:
        self.lessons.pop(indx)


class LessonItem:
    __attrib = {'title': (str,), 'practices': (int,), 'duration': (int,)}

    def __init__(self, title: str, practices: int, duration: int) -> None:
        self.title = title
        self.practices = practices
        self.duration = duration

    def __setattr__(self, key, value):
        if key in self.__attrib and type(value) in self.__attrib[key]:
            if (key == 'practices' or key == 'duration') and value <= 0:
                raise TypeError("Неверный тип присваиваемых данных.")
        elif key in self.__attrib:
            raise TypeError("Неверный тип присваиваемых данных.")

        object.__setattr__(self, key, value)

    def __getattr__(self, item):
        return False

    def __delattr__(self, item):
        if item in self.__attrib:
            raise AttributeError(f"Атрибут {item} удалять запрещено.")
        object.__delattr__(self, item)



course = Course("Python ООП")
module_1 = Module("Часть первая")
module_1.add_lesson(LessonItem("Урок 1", 7, 1000))
module_1.add_lesson(LessonItem("Урок 2", 10, 1200))
module_1.add_lesson(LessonItem("Урок 3", 5, 800))
course.add_module(module_1)
module_2 = Module("Часть вторая")
module_2.add_lesson(LessonItem("Урок 1", 7, 1000))
module_2.add_lesson(LessonItem("Урок 2", 10, 1200))
course.add_module(module_2)
