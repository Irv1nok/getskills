TYPE_OS = 1     # 1 - Windows; 2 - Linux

class DialogWindows:
    name_class = "DialogWindows"


class DialogLinux:
    name_class = "DialogLinux"



class Dialog:

    def __new__(cls, *args, **kwargs):
        if TYPE_OS == 1:
            win = super().__new__(DialogWindows)
            setattr(win, 'name', *args)
            return win
        else:
            lnx = super().__new__(DialogLinux)
            setattr(lnx, 'name', *args)
            return lnx

    def __init__(self, name):
        self.name = name

obj = Dialog('win')
print(obj)

