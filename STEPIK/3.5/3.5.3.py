from typing import Union
class TrackLine:

    def __init__(self, to_x: Union[int, float], to_y: Union[int, float], max_speed: int) -> None:
        self.to_x = to_x
        self.to_y = to_y
        self.max_speed = max_speed

    def length(self, x1, y1):
        return ((self.to_x - x1) ** 2 + (self.to_y - y1) ** 2) ** 0.5


class Track:

    def __init__(self, start_x: Union[int, float], start_y: Union[int, float]) -> None:
        self.start_x = start_x
        self.start_y = start_y
        self.track_length = []

    def add_track(self, tr: "TrackLine") -> None:
        self.track_length.append(tr)
    def get_tracks(self) -> tuple:
        return tuple(self.track_length)

    def __len__(self):
        x, y = self.start_x, self.start_y
        length = 0
        for obj in self.track_length:
            length += obj.length(x, y)
            x, y = obj.to_x, obj.to_y
            return int(length)

    def __eq__(self, other):
        return len(self) == len(other)

    def __lt__(self, other):
        return len(self) < len(other)

track1 = Track(0, 0)
track2 = Track(0, 1)
track1.add_track(TrackLine(2, 4, 100))
track1.add_track(TrackLine(5, -4, 100))
track2.add_track(TrackLine(3, 2, 90))
track2.add_track(TrackLine(10, 8, 90))
n = len(track1)
print(track1 == track2)  # маршруты равны, если равны их длины
print(track1 != track2)  # маршруты не равны, если не равны их длины
print(track1 > track2)  # True, если длина пути для track1 больше, чем для track2
print(track1 < track2)  # True, если длина пути для track1 меньше, чем для track2
print(n)
print(track2.get_tracks())