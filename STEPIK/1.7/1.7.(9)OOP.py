class AppStore:
    basket = {}

    def add_application(self, app):
        self.basket[app.name] = app
        # self.basket[id(app)] = app   # можно через id обращаться

    def remove_application(self, app):
        self.basket.pop(app.name)
        # self.basket.pop[id(app)]   # можно через id обращаться

    def block_application(self, app):
        self.basket[app.name].blocked = True

    def total_apps(self):
        return len(self.basket)


class Application:

    def __init__(self, name: str, blocked=False):
        self.name = name
        self.blocked = blocked


store = AppStore()
app_youtube = Application("Youtube")
app_GooGle = Application("Google")
store.add_application(app_youtube)
store.add_application(app_GooGle)
print(AppStore.basket)
store.remove_application(app_youtube)
print(AppStore.basket)
store.block_application(app_GooGle)
print(app_GooGle.__dict__)

