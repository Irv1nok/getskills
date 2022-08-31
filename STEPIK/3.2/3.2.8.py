class Handler:

    def __init__(self, methods=('GET,')):
        self.methods = methods

    def __call__(self, func, *args, **kwargs):
        def wrapper(request):
            res = request.get('method', 'GET')
            if res in self.methods:
                method = res.lower()
                return self.__getattribute__(method)(func, request)
            return None
        return wrapper

    def get(self, func, request, *args, **kwargs):
        return f'GET: {func(request)}'

    def post(self, func, request, *args, **kwargs):
        return f'POST: {func(request)}'



@Handler(methods=('GET', 'POST')) # по умолчанию methods = ('GET',)
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "POST", "url": "contact.html"})
print(res)