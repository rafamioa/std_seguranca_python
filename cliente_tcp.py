# -*- coding: UTF-8 -*-

import socket
import hashlib

HOST = 'localhost'     
PORT = 5000            
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
dest = (HOST, PORT)
tcp.connect(dest)

conteudo_arquivo = 'Fatec'
nome_arquivo = 'arquivo'

h = hashlib.sha256()
h.update(conteudo_arquivo.encode('UTF-8'))

mensagem_enviada = nome_arquivo + ';' + conteudo_arquivo +';'+ h.hexdigest()

tcp.send(mensagem_enviada.encode('UTF-8'))

mensagem_recebida = tcp.recv(1024)

print(mensagem_recebida.decode('UTF-8'))

tcp.close()