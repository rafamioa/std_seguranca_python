# -*- coding: UTF-8 -*-

import socket
import hashlib

HOST = ''              
PORT = 5000            
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
orig = (HOST, PORT)
tcp.bind(orig)
tcp.listen(1)         
while True:
    conexao, cliente = tcp.accept()        
    print ('Concetado por ', cliente)

    mensagem_recebida = conexao.recv(1024)            
    mensagem_recebida =  mensagem_recebida.decode('UTF-8')      
    valores = mensagem_recebida.split(';')              
    h = hashlib.sha256()
    h.update(valores[1].encode('UTF-8'))
    teste_hash = h.hexdigest()
    
    if teste_hash == valores[2]:
        file = open(valores[0] + '.txt', 'w')
        file.write(valores[1])
        file.close()
    
        mensagem_enviada = 'Recebido pelo servidor'
        conexao.send(mensagem_enviada.encode('UTF-8'))
    else:
        mensagem_enviada = 'Erro ao validar o hash token'
        conexao.send(mensagem_enviada.encode('UTF-8'))
        
    print ('Finalizando conexão do cliente', cliente)
    conexao.close()
