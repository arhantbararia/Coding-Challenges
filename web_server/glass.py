##using sockets to bind to a port and listen for requests
import socket



if __name__ == "__main__":
    serversocket = socket.socket(socket.AF_INET , socket.SOCK_STREAM)

    serversocket.bind(('localhost' , 80))
    serversocket.listen()
    (clientsocket, cli_addr) = serversocket.accept()

    print("hello world")
    