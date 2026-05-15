# -*- coding: utf-8 -*-
#Biblioteca sockets
import socket

#Porta do servidor
port = 8084

#Mensagem que o servidor envia
msg = input('Mensagem a ser enviada (SERVIDOR -> CLIENTE): ')

#Objeto socket
serv  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associa o socket a uma porta local
serv.bind(('0.0.0.0',port))
serv.listen()

#Servidor fica aguardando conexões
while True:
    print(f'== Servidor aguardando conexões na porta {port} ==')
    conn, addr = serv.accept()
    print(f'== Conexao recebida de {addr} ==')
 
    #Recebe os dados
    data = conn.recv(4096)
    #Caso não haja dados, encerra a conexao
    if not data: break

    #Trata os dados recebidos
    from_client = data
    print('== Dados recebidos: ==')
    print(from_client.decode())

    #Envia uma mensagem
    print('== Enviando mensagem ==')
    conn.send(from_client.upper())
    print('== Mensagem enviada ==')

    #Fecha a conexao
    conn.close()
    print('== Cliente desconectado ==')
