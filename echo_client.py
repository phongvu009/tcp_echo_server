import socket
#define Where to connect to
HOST = '127.0.0.1' #loopback interface or localhost or ::1
PORT = 6542

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST,PORT))
    #send message byte to server
    s.sendall(b"This is very first message need to send to the server. 123$%^&!@#")
    #get reply back
    data = s.recv(1024)

print(f"get reply back : {data}")