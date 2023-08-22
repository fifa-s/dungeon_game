import socket
import threading
import pickle
import multiprocessing as mp
import networking.ipv4 as ipv4
from .send import send
from .network_constants import *
from .id_int_convertion import int_to_id

class Server:
    
    def __init__(self):
        manager = mp.Manager()
        self.data = manager.dict()
        self.server_process = _ServerProcess()
        self.id = self.server_process.get_id()
        self.process = mp.Process(target=self.server_process.run, args=[self.data])

class _ServerProcess:
    
    def __init__(self):
        self.ip = socket.gethostbyname(socket.gethostname())
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._sock.bind((self.ip, 0))
        self.port = self._sock.getsockname()[1]
        
    def get_id(self):
        """returns the id that the Client class from client.py takes"""
        ip_int = ipv4.ipv4_to_int(self.ip)
        id_int =  (ip_int << 16 ) + self.port
        return int_to_id(id_int)
    
    def get_msg(self, connection):
        msg_length = pickle.loads(connection.recv(HEADER))
        if not msg_length: return
        msg_length: int = int(msg_length)
        return pickle.loads(connection.recv(msg_length))
    
    
    def handle_client(self, connection, address):
        print(f"[SERVER] New connection: {address}")
        while True:
            try: 
                msg = self.get_msg(connection)
            except Exception as e:
                print(f"[SERVER] Disconnecting {address}: {e}")
                connection.close()
                return
                
            if msg == None: continue
            if msg == DISCONNECT_MESSAGE: break
            if msg == REQUEST_MESSAGE:
                send(connection, self.data.copy())
                continue

            self.data[address] = msg
            #print(f"[{address}]: {msg}")
    
        connection.close()
        print(f"[{address}] disconnected")
    
    def run(self, data):
        self.data = data
        self._sock.listen()
        print(f"[SERVER] Listening on {self.ip} and on port {self.port}.")
        while True:
            connection, address = self._sock.accept()
            thread = threading.Thread(target=self.handle_client, args=(connection, address))
            thread.start()
            print(f"[SERVER] Active connections: {threading.active_count() - 1}")

if __name__ == "__main__":
    server = Server()
