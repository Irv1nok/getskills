class Book:

    def __init__(self, title: str = '', author: str = '', pages: int = 0, year: int = 0) -> None:
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year

    def __setattr__(self, key, value) -> None:
        if key == 'title' and type(value) is str:
            object.__setattr__(self, key, value)

        elif key == 'author' and type(value) is str:
            object.__setattr__(self, key, value)

        elif key == 'pages' and type(value) is int:
            object.__setattr__(self, key, value)

        elif key == 'year' and type(value) is int:
            object.__setattr__(self, key, value)
        else:
            raise TypeError('Неверный тип присваиваемых данных.')

book = Book('Сергей Балакирев', 'Python ООП', 123, 2022)


