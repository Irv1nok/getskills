class Player:

    def __init__(self, name: str, old: int, score: int):
        self.name = name
        self.old = int(old)
        self.score = int(score)

    def __bool__(self) -> bool:
        return self.score > 0


lst_in = ['Балакирев; 34; 2048',
            'Mediel; 27; 0',
            'Влад; 18; 9012',
            'Nina P; 33; 0']

players = [Player(*p.split('; ')) for p in lst_in]
players_filtered = list(filter(bool, players))


