from random import choice, randint

class Line:

    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:

    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:

    def __init__(self, a=0, b=0, c=0, d=0):
        self.sp = (a, b)
        self.ep = (c, d)

def rndz_objects():
    def rndz_args():
        args = [0, 0, 0, 0]
        for i in range(len(args)):
            x = randint(0, 10)
            args[i] = x
        return args

    elements = []
    for _ in range(217):
        elements.append(choice([Line, Rect, Ellipse])(*rndz_args()))
    return elements

def update(el):
    for element in el:
        if isinstance(element, Line):
            element.ep = (0, 0)
            element.sp = (0, 0)
    return el

elements = rndz_objects()
update(elements)


print(elements[0].__dict__)

# import random
#
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# classes = [Line, Rect, Ellipse]
# elements = [random.choice(classes)(*[random.randint(1, 100) for i in '____']) for i in range(217)]
# for i, y in enumerate(elements):
#     if isinstance(y, Line):
#         elements[i].sp = (0, 0);
#         elements[i].ep = (0, 0)



# from random import choice, randint
#
# class Line:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# class Rect:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
# class Ellipse:
#     def __init__(self, a, b, c, d):
#         self.sp = (a, b)
#         self.ep = (c, d)
#
#
# elements = [choice([Line,Rect,Ellipse])(*[randint(0,1000) for _ in '1234']) for _ in range(217)]
# elements = [Line(0,0,0,0) if type(x) == Line else x for x in elements]