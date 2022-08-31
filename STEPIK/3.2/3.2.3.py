from typing import Any


class ImageFileAcceptor:

    def __init__(self, extensions: str) -> None:
        self.extensions = extensions

    def __call__(self, *args, **kwargs) -> Any:
        return [f_name for f_name in args for ext in self.extensions if ('.' + ext) in f_name]

    # def __call__(self, filename, *args, **kwargs):
    #     return filename.split('.')[-1] in self.__extensions

# filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
# acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
# image_filenames = filter(acceptor, filenames)
# print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]
fs = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.8.jpg", "forest.jpeg", "eq_1.png", "eq_2.png", "my.html", "data.shtml"]
acceptor = ImageFileAcceptor(("jpg", "png"))
res = filter(acceptor, fs)

assert set(res) == set(["boat.jpg", "web.png", "ava.8.jpg", "eq_1.png", "eq_2.png"]), "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"

acceptor = ImageFileAcceptor(("jpeg", "html"))
res = filter(acceptor, fs)
assert set(res) == set(["forest.jpeg", "my.html"]), "с помощью объекта класса ImageFileAcceptor был сформирован неверный список файлов"
