class Router:
    app: dict = {}

    @classmethod
    def get(cls, path):
        return cls.app.get(path)

    @classmethod
    def add_callback(cls, path, func):
        cls.app[path] = func


class Callback:

    def __init__(self, path, router_cls: Router):
        self.path = path
        self.route_cls = router_cls

    def __call__(self, func):
        self.route_cls.add_callback(self.path, func)