"""
        Script for Creating server, accept connections and search for strings in a specific file
"""
import socket 
import threading
import time
import os
import subprocess
import ahocorasick
import datetime
from config import HEADER, PORT ,FORMAT ,DISCONNECT_MESSAGE, LINUX_PATH, REREAD_ON_QUERY, new_line

SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR) 

def main():
    """Launcher"""
    print("[STARTING] server is starting...")
    try:
        start()
    except Exception as e:
        print(f'[ERROR] cannot start server {e}...')

def start():
    """
        Listens for connections and creates a thread for them
    """
    if REREAD_ON_QUERY:
        search_function = search_file
        automaton = None
    else:
        search_function = search_list
        file_lines = file_to_list()
        try:
            automaton = ahocorasick.Automaton()
            for idx, key in enumerate(file_to_list()):
                automaton.add_word(key, (idx, key))
        except Exception as e:
            print(f'[ERROR] cannot make trie {e}, restarting!')
            start()

    server.listen()
    print(f"[LISTENING] Server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()

        try:
            thread = threading.Thread(target=handle_client, args=(conn, addr, search_function, automaton))
            thread.start()
        except Exception as e:
            print(f"[ERROR] error while creating new thread!")

        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

def handle_client(conn, addr, search_function, automaton):
    """
        Handles client's search queries

        Args:
                :param conn: client address
                :param addr: connections host and port
                :param search_function: search function used
                :param automator: automator if REREAD_ON_QUERY is False else None

        Returns:
                :returns: None
    """
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        try:
            msg = conn.recv(HEADER).decode(FORMAT)
        except Exception as e:
            print('[ERROR] Input error {e}')

        if msg:
            ts = datetime.datetime.now().timestamp()
            if len(msg) > 50:
                print(f"[DEBUG] {addr} Message to long {ts}")
                conn.send("Message to long!\n".encode(FORMAT))

            elif msg == DISCONNECT_MESSAGE:
                connected = False
                print(f"[DEBUG] {addr} {msg} {ts}")
                conn.send("Disconnected!".encode(FORMAT))

            else:
                exec_time, search = search_function(msg, automaton)
                print(f"[DEBUG] {msg.replace(new_line, '')} {addr} {exec_time} {ts}")
                conn.send(search.encode(FORMAT))

    conn.close()

def exec_time(func):
    """
        Mesures execution time

        Args:
                :param func: function to process

        Returns:
                :returns: execution time and function's output
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        elapsed = "%.4f" % ((time.time() - start_time) * 100) + " ms"
        return elapsed, result
    return wrapper

@exec_time
def search_file(string, automaton):
    """
        Searches for string in file

        Args:
                :param string: string to process
                :param automaton: unused, always None

        Returns:
                :returns: string's existance in file
    """
    args = f"grep -rnw '{LINUX_PATH}' -e '{string}'"
    try:
        with open(os.devnull, 'wb') as devnull:
            if subprocess.check_call(args, stdout=devnull, stderr=subprocess.STDOUT, shell=True) == 0:
                return "STRING EXISTS\n"
    except:
        pass
    return "STRING NOT FOUND\n"

@exec_time
def search_list(string, automaton):
    """
        Searches for string in the trie

        Args:
                :param string: string to process
                :param automaton: trie holding index, strings in file

        Returns:
                :returns: string's existance in file
    """
    if string in automaton:
        return "STRING EXISTS\n"
    return "STRING NOT FOUND\n"

def file_to_list():
    """
        Reads file lines

        Returns:
                :returns: list of file lines
    """
    try:
        with open(LINUX_PATH, "r") as text_file:
            return text_file.read().splitlines()
    except Exception as e:
        print(f'[ERROR] Error while reading file! {e}')

# Entry point of the application
if __name__ == '__main__':
        main()