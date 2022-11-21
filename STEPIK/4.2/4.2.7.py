class VideoItem:

    def __init__(self, title: str, descr: str, path: str):
        self.title = title
        self.descr = descr
        self.path = path
        self.rating = VideoRating()


class VideoRating:

    def __init__(self):
        self.__rating = 0

    @property
    def rating(self):
        return self.__rating

    @rating.setter
    def rating(self, value):
        if not value < 0 or value > 5:
            self.__rating = value
        else:
            raise ValueError('неверное присваиваемое значение')


v = VideoItem('Курс по Python ООП', 'Подробный курс по Python ООР', 'D:/videos/python_oop.mp4')
print(v.rating.rating)  # 0
v.rating.rating = 5
print(v.rating.rating)  # 5
title = v.title
descr = v.descr
# v.rating.rating = 6  # ValueError
