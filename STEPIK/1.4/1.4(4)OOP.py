class Point:

    def __init__(self, x, y, color="black"):
        self.x = x
        self.y = y
        self.color = color

points = [Point(i*2+1,i*2+1,'yellow' if i%2 else 'black') for i in range(1000)]
print(points[0].__dict__)
print(points[1].__dict__)
print(points[2].__dict__)
print(points[3].__dict__)
print(points[4].__dict__)
print(points[5].__dict__)

