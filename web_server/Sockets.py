import socket

class MySocket:

    def __init__(self , sock= None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

        else:
            self.socke = sock

    
    def connect(self , host , port):
        self.sock.connect((host, port))

    
    def listen(self, backlog):
        self.sock.listen(backlog)

    def accept(self):
        client_sock , client_addr  = self.sock.accept()
    
        return client_sock
    

    def mysend(self, msg):



