import sys

class StreamData :
    def create(self, fields, lst_values):
        if len(fields) == len(lst_values):
            for i, field in enumerate(fields):
                setattr(self, field, lst_values[i])
            return True
        else:
            return False




class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = ['1', 'Good', '2']
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        print(sd.__dict__)
        print(res)
        return sd, res


sr = StreamReader()
data, result = sr.readlines()
print(data.__dict__)



