import socket
HOST = ""
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)
while True:
    con, cliente = tcp.accept()
    print("conectado por", cliente)
    while True:
        msg = con.recv(1024)
        if not msg: break
        print(cliente, msg)
    print("finalizando conexão do cliente", cliente)
    con.close()
