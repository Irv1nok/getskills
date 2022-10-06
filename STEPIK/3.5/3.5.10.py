from typing import Union


class Box:

    def __init__(self):
        self.inbox = []

    def add_thing(self, obj: "Thing") -> None:
        self.inbox.append(obj)

    def get_things(self) -> list:
        return self.inbox

    def __eq__(self, other: "Box"):
        if len(self.inbox) == len(other.inbox):
            res = self.inbox.copy()
            for obj in self.inbox:
                for obj2 in other.inbox:
                    if obj == obj2:
                        try:
                            res.remove(obj)
                        except ValueError:
                            return False

            return True if not res else False


class Thing:

    def __init__(self, name: str, mass: Union[int, float]):
        self.name = name
        self.mass = mass

    def __eq__(self, other: "Thing") -> bool:
        return self.name.lower() == other.name.lower() and self.mass == other.mass


b1 = Box()
b2 = Box()

b1.add_thing(Thing('мел', 100))
b1.add_thing(Thing('тряпка', 200))
b1.add_thing(Thing('доска', 2000))

b2.add_thing(Thing('тряпка', 200))
b2.add_thing(Thing('мел', 100))
b2.add_thing(Thing('доска', 2000))

res = b1 == b2  # True
print(res)
