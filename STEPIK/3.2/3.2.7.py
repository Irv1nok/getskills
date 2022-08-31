class HandlerGET:

    def __init__(self, func):
        self.func = func

    def __call__(self, request, *args, **kwargs):

        return self.get(self.func, request)

    def get(self, func, request, *args, **kwargs):
        if not request.get('method'):
            return f'GET: {func(request)}'
        elif request['method'] != 'GET':
            return None

        return f'GET: {func(request)}'


@HandlerGET
def contact(request):
    return "Сергей Балакирев"

res = contact({"method": "GET", "url": "contact.html"})
print(res)