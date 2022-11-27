from typing import Union, Dict


class Aircraft:

    def __init__(self, model: str, mass: Union[int, float], speed: Union[int, float], top: Union[int, float]):
        self._model = model
        self._mass = mass
        self._speed = speed
        self._top = top

    def __setattr__(self, name, value):
        if name == "_model" and type(value) != str:
            raise TypeError('неверный тип аргумента')

        if name in ("_mass", "_speed", "_top"):
            if type(value) not in (int, float) or value <= 0:
                raise TypeError('неверный тип аргумента')

        object.__setattr__(self, name, value)


class PassengerAircraft(Aircraft):

    def __init__(self, model: str,
                 mass: Union[int, float],
                 speed: Union[int, float],
                 top: Union[int, float],
                 chairs: Union[int, float]):
        super().__init__(model, mass, speed, top)
        if type(chairs) != int:
            raise TypeError('неверный тип аргумента')
        self._chairs = chairs


class WarPlane(Aircraft):

    def __init__(self, model: str,
                 mass: Union[int, float],
                 speed: Union[int, float],
                 top: Union[int, float],
                 weapons: Dict[str, int]):
        super().__init__(model, mass, speed, top)
        if type(weapons) != dict or not all([type(value) == int for value in weapons.values()]):
            raise TypeError('неверный тип аргумента')
        self._weapons = weapons


planes = [PassengerAircraft('МС-21', 1250, 8000, 12000.5, 140),
          PassengerAircraft('SuperJet', 1145, 8640, 11034, 80),
          WarPlane('Миг-35', 7034, 25000, 2000, {"ракета": 4, "бомба": 10}),
          WarPlane('Су-35', 7034, 34000, 2400, {"ракета": 4, "бомба": 7})]
