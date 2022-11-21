class Singleton:
    __INSTANCE_CHILD = None
    __INSTANCE_SINGLETON = None

    def __new__(cls, *args, **kwargs):
        if cls == Singleton:
            if cls.__INSTANCE_SINGLETON is None:
                cls.__INSTANCE_SINGLETON = super().__new__(cls)
            return cls.__INSTANCE_SINGLETON

        if cls.__INSTANCE_CHILD is None:
            cls.__INSTANCE_CHILD = super().__new__(cls)
            setattr(cls.__INSTANCE_CHILD, 'name', *args)
        return cls.__INSTANCE_CHILD


class Game(Singleton):
    pass

game1 = Game('Saper')
print(game1.__dict__)
game2 = Game('Durak')
print(game2.__dict__)