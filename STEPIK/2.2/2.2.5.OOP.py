class WindowDlg:

    def __init__(self, заголовок_окна, ширина, высота):
        self.__title = заголовок_окна
        self.__width = ширина
        self.__height = высота

    def show(self):
        print(f'{self.__title}:{self.__width},{self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, w):
        print('Call setter width')
        if isinstance(w, int) and 0 < w < 10_000:
            self.__width = w
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, h):
        print('Call setter height')
        if isinstance(h, int) and 0 < h < 10_000:
            self.__height = h
            self.show()

wnd = WindowDlg(1, 2, 3)

wnd.height = 5
print(wnd.__dict__)