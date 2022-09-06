class PolyLine:

    def __init__(self, *args):
        self.args = list(args)

    def add_coord(self, x: int, y: int):
        self.args.append((x, y))

    def remove_coord(self, indx: int):
        self.args.pop(indx)

    def get_coords(self) -> list:
        return self.args


p = PolyLine((1, 2), (3, 5), (0, 10))
p.add_coord(2, 2)
p.remove_coord(2)
print(p.get_coords())