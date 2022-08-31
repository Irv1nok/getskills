from typing import Union


class Bag:

    def __init__(self, max_weight: int) -> None:
        self.max_weight = max_weight
        self.__things = []
        self.allowed_weight = max_weight

    @property
    def things(self) -> list:
        return self.__things

    def add_thing(self, thing: 'Thing') -> None:
        self.allowed_weight -= thing.weight
        if self.allowed_weight >= 0:
            self.__things.append(thing)

    def remove_thing(self, indx: int) -> None:
        self.allowed_weight += self.__things[indx].weight
        self.__things.pop(indx)

    def get_total_weight(self) -> Union[int, float]:
        if self.__things:
            return sum([obj.weight for obj in self.__things])
        return []


class Thing:

    def __init__(self, name: str, weight: Union[int, float]):
        self.name = name
        self.weight = weight

bag = Bag(1000)
bag.add_thing(Thing('fire', 10))

bag.remove_thing(0)
print(bag.get_total_weight())
