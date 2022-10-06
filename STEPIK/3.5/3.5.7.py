filenames = ["boat.jpg", "ans.web.png", "text.txt",
             "www.python.doc", "my.ava.jpg", "forest.jpeg",
             "eq_1.png", "eq_2.xls"]


class FileAcceptor:

    def __init__(self, *args) -> None:
        self.f_names = list(args)

    def __call__(self, filename: str) -> bool:
        return filename.split('.')[-1] in self.f_names

    def __add__(self, other: "FileAcceptor") -> "FileAcceptor":
        return FileAcceptor(*self.f_names + other.f_names)


acceptor_images = FileAcceptor("jpg", "jpeg", "png")
acceptor_docs = FileAcceptor("txt", "doc", "xls")

file = acceptor_images + acceptor_docs
filenames = list(filter(acceptor_images, filenames))
print(filenames)
