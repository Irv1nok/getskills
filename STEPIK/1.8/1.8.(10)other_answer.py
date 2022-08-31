class Data:

    def __init__(self, data, ip_destination):
        self.data = data
        self.ip = ip_destination  # ip of destination


class Server:
    __number_of_servers = 0

    def __init__(self):
        Server.__number_of_servers += 1
        self.ip = Server.__number_of_servers
        self.buffer = []
        self.main_router: Router = None

    def send_data(self, data: Data):
        self.main_router.buffer.append(data)

    def get_data(self):
        buffer_before_cleaning = self.buffer.copy()
        self.buffer.clear()
        return buffer_before_cleaning

    def get_ip(self):
        return self.ip


class Router:

    def __init__(self):
        self.servers = dict()
        self.buffer = []

    def link(self, server):
        if server.ip not in self.servers:
            self.servers[server.ip] = server
            server.main_router = self

    def unlink(self, server):
        if server in self.servers:
            server.main_router = None
            del self.servers[server.ip]

    def send_data(self):
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
            else:
                pass  # here we should raise error destination unreachable
        self.buffer.clear()


router = Router()
sv_from = Server()
sv_from2 = Server()
router.link(sv_from)
router.link(sv_from2)
router.link(Server())
router.link(Server())
sv_to = Server()
router.link(sv_to)
sv_from.send_data(Data("Hello", sv_to.get_ip()))
sv_from2.send_data(Data("Hello", sv_to.get_ip()))
sv_to.send_data(Data("Hi", sv_from.get_ip()))
# print(router.buffer)
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
# print(msg_lst_from)
# print(msg_lst_to)
# print(sv_from.__dict__)
# print(sv_from2.__dict__)
# print(sv_to.__dict__)