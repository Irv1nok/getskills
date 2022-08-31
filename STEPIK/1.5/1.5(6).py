class Graph:

    def __init__(self, data, is_show=True):
        self.data = data
        self.is_show = is_show

    def set_data(self, data):
        self.data = data

    def show_table(self):
        if self.is_show == True:
            print(*self.data)
        else:
            print("Отображение данных закрыто")

    def show_graph(self):
        if self.is_show == True:
            print("Графическое отображение данных:", *self.data)
        else:
            print("Отображение данных закрыто")

    def show_bar(self):
        if self.is_show == True:
            print("Столбчатая диаграмма:", *self.data)
        else:
            print("Отображение данных закрыто")

    def set_show(self, fl_show):
        self.is_show = fl_show

data_graph = [8, 11, 10, -32, 0, 7, 18]
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()

