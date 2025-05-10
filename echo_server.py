import socket
import logging

logging.basicConfig(level=logging.INFO)

#define HOST, PORT 
HOST = '127.0.0.1' # Standard loopback interface address
PORT = 6542

#create socket with context manager
#using with - no need to close socket manually
#socket.AF_INET : Ipv4 protocol
#socket.SOCKET_STREAM : protocol - socket type
#using while True  to accept multiple connections. it will serve one by one client 
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST,PORT)) # socket with specific network interface - application can be talked at port
        #listen 
        s.listen()
        logging.info(f"Server started !!!- listening on {HOST}:{PORT}")
        #accept return a new socket object
        client_socket, addr = s.accept() #block until connection
        #has connection
        with client_socket:
            print(f"Connected by {addr}")
            #
            while True:
                data = client_socket.recv(1024)
                if not data: #if b'' close connection
                    break
                client_socket.sendall(data)



