
import socket
import random
from config import HEADER, PORT, FORMAT, DISCONNECT_MESSAGE, SERVER
from threading import Thread
import time

exists = [
    '22;0;6;16;0;17;4;0;',
    '22;0;6;16;0;17;4;0;',
    '22;0;6;16;0;17;4;0;',
    '23;0;6;26;0;20;3;0;',
    '24;0;21;16;0;17;3;0;',
    '25;0;21;28;0;20;3;0;',
    '25;0;21;28;0;20;3;0;',
    '1;0;6;26;0;7;3;0;',
    '2;0;16;21;0;24;3;0;',
    '3;0;1;26;0;17;5;0;',
    '3;0;1;26;0;17;5;0;',
    '4;0;1;16;0;6;3;0;',
    '16;0;23;11;0;20;3;0;'
]

doesnt_exists = [
    'cant_be_there',
    'no_no_no',
    'doesnt_ exists'
]

def send():
    ADDR = (SERVER, PORT)

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)

    while True:
        for i in range(10):
            if bool(random.getrandbits(1)):
                String = random.choice(exists)
            else:
                String = random.choice(doesnt_exists)

            message = String.encode(FORMAT)
            msg_length = len(message)
            send_length = str(msg_length).encode(FORMAT)
            send_length += b' ' * (HEADER - len(send_length))
            client.send(send_length)
            client.send(message)

        time.sleep(1)

def main():
    for i in range(800):
        Thread(target = send).start()


main()
