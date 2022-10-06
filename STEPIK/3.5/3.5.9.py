from typing import Union


class Body:

    def __init__(self, name: 'str', ro: Union[int, float], volume: Union[int, float]) -> None:
        self.name = name
        self.ro = ro
        self.volume = volume

    def calc_mass(self):
        return self.ro * self.volume

    def __lt__(self, other: "Body") -> bool:
        sc = other if isinstance(other, (int, float)) else other.calc_mass()
        return self.calc_mass() < sc

    def __eq__(self, other: "Body") -> bool:
        sc = other if isinstance(other, (int, float)) else other.calc_mass()
        return self.calc_mass() == sc

    def __gt__(self, other: "Body") -> bool:
        sc = other if isinstance(other, (int, float)) else other.calc_mass()
        return self.calc_mass() > sc
