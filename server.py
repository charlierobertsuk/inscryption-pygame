# freecodecamp - youtube - python multiplayer game development totorial

import socket, sys # socket and thread handle connections to the server
from _thread import *

server = "192.168.0.114" # cmd - ipconfig - ipv4
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2) # opens up the port (if empty, unlimited people. 2 means only 2 people or 1 for 2 ppl i cant remember if its 0,1 or 1,2)
print("Waiting for a connection, Server Started")

def threaded_client(conn):
    
    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Recieved", reply)
                print("Sendong", reply)

            conn.sendall(str.encode(reply))
        except:
            break


while True:
    conn, addr = s.accept() # accepte any incoming connections
    print("Connected to", addr)

    start_new_thread(threaded_client, (conn, ))
