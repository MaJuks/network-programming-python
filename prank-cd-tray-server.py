import os
import socket
port = 8084

#object Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#associa the socket for a port
server.bind("0.0.0.0",port)
server.listen()
cmd = "eject; sleep 0.5s; eject -t; sleep 0.5s"
while True:
    print(f"***Server waiting in the port {port}***")

    #accept the connection
    conn, addr = server.accept()
    print(f"== connection received OF {addr} ==")
    os.system(cmd)

    
    #close the connection
    conn.close()
    print("== client disconnected == ")

