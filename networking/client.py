import socket
import pickle
import multiprocessing as mp
from pygame.time import Clock
import networking.ipv4 as ipv4
from .send import send
from .network_constants import  *
from .id_int_convertion import id_to_int

MSG_PER_SECOND = 8

class Client:
    
    def __init__(self, id: str):
        manager = mp.Manager()
        self.my_data = manager.dict()
        self.server_data = manager.dict()
        self.client_process = _ClientProcess(id)
        self.id = id
        self.process = mp.Process(target=self.clientprocess.run, args=[self.my_data, self.server_data])

class _ClientProcess:
    
    def __init__(self, id: str):
        """id: Server.get_id()"""
        self._set_id(id)
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f"ip: {self.ip}\nport: {self.port}")
        self._sock.connect((self.ip, self.port))
        self.clock = Clock()
        self.running = True
        
    def _set_id(self, id: str):
        id_int = id_to_int(id)
        try:
            self.port = id_int & 0xFFFF
            self.ip = ipv4.int_to_ipv4((id_int >> 16))
            
        except:
            raise ValueError("Invalid id")
        
    def request_data(self):
        self.send(REQUEST_MESSAGE)
        msg_length = pickle.loads(self._sock.recv(HEADER))
        if not msg_length: return
        msg_length: int = int(msg_length)
        return pickle.loads(self._sock.recv(msg_length))

    def send(self, message):
        send(self._sock, message)
        
    def run(self, my_data, server_data):
        self.my_data = my_data
        self.server_data = server_data
        while self.running:
            self.send(self.my_data)
            self.server_data = self.request_data()
            self.clock.tick(MSG_PER_SECOND)
        

if __name__ == "__main__":
    client = Client(input("id: "))
    client.my_data["messages"] = []
    while True:
        input_ = input("message: ")
        client.my_data["messages"].append(input_)
        print(f"server_data: {client.server_data}")