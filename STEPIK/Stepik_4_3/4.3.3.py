class Book:


    def __init__(self, title: str, author: str, pages: int, year: int):
        self.title = title
        self.author = author
        self.pages = pages
        self.year = year


class DigitBook(Book):

    def __init__(self, title: str, author: str, pages: int, year: int, size: int, frm:str):
        super().__init__(title, author, pages, year)
        self.size = size
        self.frm = frm


