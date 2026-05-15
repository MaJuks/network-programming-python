from configparser import Interpolation
import socket
import pickle

#port and address of server
port = 8084
dest = "192.168.246.75"

#object Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect in server
print(f"-- Connecting to {dest} --")
client.connect((dest, port))

client.close()

