import socket

#Porta do servidor
port = int(input('port = '))

#Objeto socket
serv  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Associa o socket a uma porta local
serv.bind(('0.0.0.0',port))
serv.listen()

while True:
    #Servidor fica aguardando conexões
    print(f'== Servidor aguardando conexões na porta {port} ==')
    conn, addr = serv.accept()
    print(f'== Conexao recebida de {addr} ==')

    while True:
        #Recebe os dados
        data = conn.recv(4096)
        from_client = data
        print('Cliente: ', from_client.decode())

        if from_client.decode() == 'logout':
            conn.close()
            print('== Cliente desconectado ==')
            break
        else:
            #Mensagem que o servidor envia
            msg = input('Server: ')

            #Envia uma mensagem
            conn.send(msg.encode())