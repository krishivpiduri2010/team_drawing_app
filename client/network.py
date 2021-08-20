import pickle
import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '192.168.0.103'
        self.port = 5000
        self.addr = (self.server, self.port)
        self.initial_value = self.connect()
        self.recv_size = 2048

    def connect(self):
        self.client.connect(self.addr)
        return self.client.recv(2048).decode()

    def send(self, data, encode: str):
        if encode.lower() == 'pickle':
            data = pickle.dumps(data)
        else:
            data = data.encode()
        self.client.send(data)
        decode_format = self.client.recv(2048).decode()
        if decode_format.lower() == 'pickle':
            return pickle.loads(self.client.recv(2048))
        else:
            return self.client.recv(2048).decode()
    def disconnect(self):
        self.client.close()