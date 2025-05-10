import socket

HOST = '127.0.0.1'
PORT = 6532

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    #send message byte to server
    s.sendall(b"Hello, world")
    #get reply back
    data = s.recv(1024)

print(f"get reply back : {data}")