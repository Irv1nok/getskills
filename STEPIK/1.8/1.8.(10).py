class Data:

    def __init__(self, data: str, ip: int):
        self.data = data
        self.ip = ip

class Server:
    __IP_POOL = 0

    def __new__(cls, *args, **kwargs):
        cls.__IP_POOL += 1
        return super().__new__(cls)

    def __init__(self) -> None:
        self.ip = self.__IP_POOL
        self.buffer = list()
        self.main_router = Router

    def send_data(self, data: Data) -> None:
        self.main_router.buffer.append(data)

    def get_data(self) -> list:
        if self.buffer:
            msg = self.buffer.copy()
            self.buffer.clear()
            return msg
        else:
            return []
        self.buffer.clear()

    def get_ip(self) -> int:
        return self.ip

class Router:
    __SERVERS_LINK = dict()

    def __init__(self) -> None:
        self.buffer = list()

    def link(self, server: Server) -> None:
        server.main_router = self
        self.__SERVERS_LINK[server.ip] = server

    def unlink(self, server: Server) -> None:
        server.main_router = None
        del self.__SERVERS_LINK[server.ip]

    def send_data(self) -> None:
        for msg in self.buffer:
            for ip, data in self.__SERVERS_LINK.items():
                if msg.ip == ip:
                    data.buffer.append(msg)
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
router.send_data()
msg_lst_from = sv_from.get_data()
msg_lst_to = sv_to.get_data()
print(msg_lst_from)
print(msg_lst_to)
print(sv_from.__dict__)
print(sv_from2.__dict__)
print(sv_to.__dict__)






