
import socket
from config import HEADER, PORT, FORMAT, DISCONNECT_MESSAGE, SERVER

ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))

def main():
    while True:
        String = str(input("String: -"))
        send(String)
        if String == DISCONNECT_MESSAGE:
            break

main()
