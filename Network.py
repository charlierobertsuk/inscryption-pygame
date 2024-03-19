import socket

class network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = "192.168.0.114" # cmd - ipconfig - ipv4 - NOTE: needs to be same as server.py address
        self.port = 5555 # also needs to be the same
        self.addr = (self.server, self.port)
        self.id = self.connect()
        print (self.id)

        def connect(self):
            try:
                self.client.connect(self.addr)
                return self.client.recv(2046).decode()
            except:
                pass

n = network()