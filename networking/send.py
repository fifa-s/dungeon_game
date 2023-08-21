import pickle
from networking.network_constants import HEADER

def send(sock, message):
    msg = pickle.dumps(message)
    msg_len = len(msg)
    send_len = pickle.dumps(msg_len)
    if len(send_len) > HEADER:
        raise ValueError(f"message too large")
    send_len += b' ' * (HEADER  - len(send_len))
    sock.send(send_len)
    sock.send(msg)