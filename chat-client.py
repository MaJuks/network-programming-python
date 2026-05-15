import socket

#Porta do servidor
port = int(input('port = '))

#Endereço do servidor
dest = '192.168.246.71'
#input('dest = ')

#Objeto socker
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecta ao servidor
print(f'== Conectando a {dest}:{port} ==')
client.connect((dest, port))

while True:
    #Mensagem que o cliente envia
    msg = input('Cliente: ')

    #Envia mensagem ao servidor
    client.send(msg.encode())

    if msg == 'logout':
        print('== Cliente desconectado ==')
        break
    else:    
        #Recebe mensagem do servidor
        from_server = client.recv(4096)
        print('Server: ', from_server.decode())