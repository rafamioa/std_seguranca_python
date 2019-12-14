
import socket

HOST = "127.0.0.1"
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)
tcp.connect(dest)
print("para sair use ctrl+x\n")
msg = input()
while msg != "\x18":
    tcp.send(msg)
    msg = input()
tcp.close()
