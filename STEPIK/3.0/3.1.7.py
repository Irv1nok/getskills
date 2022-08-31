class SmartPhone:

    def __init__(self, model: str) -> None:
        self.model = model
        self.apps = []

    def add_app(self, app) -> None:
        if type(app) not in map(type, self.apps):
            self.apps.append(app)

    def remove_app(self, app) -> None:
        self.apps.remove(app)


class AppVK:

    def __init__(self) -> None:
        self.name = 'ВКонтакте'


class AppYouTube:

    def __init__(self, memory: int) -> None:
        self.name = 'YouTube'
        self.memory = memory


class AppPhone:

    def __init__(self, phone_list: dict) -> None:
        self.name = 'Phone'
        self.phone_list = phone_list


sm = SmartPhone("Honor 1.0")
sm.add_app(AppVK())
sm.add_app(AppVK())  # второй раз добавляться не должно
sm.add_app(AppYouTube(2048))
for a in sm.apps:
    print(a.name)
print(type(sm.apps[0]))
print(type(sm.apps[1]))
print(type(sm.apps[2]))