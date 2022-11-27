class SoftList(list):

    def __init__(self, string: str):
        super().__init__(string)

    def __getitem__(self, index):
        if index < -1 or index >= len(self):
            return False
        return super().__getitem__(index)

    def __setitem__(self, index, value):
        if index < -1 or index >= len(self):
            return False
        super().__setitem__(index, value)



sl = SoftList("python")
print(sl)
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(sl[6]) # False
print(sl[-7]) # False