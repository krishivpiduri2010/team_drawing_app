import _thread
from game import *
import socket

connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server='192.168.0.103'
port=5000
connection.bind((server,port))
print('[SERVER STARTED] LISTENING')
connection.listen()

def threaded_client(client:socket.socket):
    client.send('hello'.encode())
while True:
    client,addr=connection.accept()
    print(F'[NEW CONNECTION]{addr} CONNECTED')
    _thread.start_new_thread(threaded_client,(client,))
