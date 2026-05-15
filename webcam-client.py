from configparser import Interpolation
import cv2
import socket
import pickle

#port and address of server
port = 8084
dest = "192.168.246.66"

#object Socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#connect in server
print(f"-- Connecting to {dest} --")
client.connect((dest, port))

#receive date of server
data = []
while True:
    pacote = client.recv(4096)
    if not pacote: break
    data.append(pacote)

#dispack the frame received
frame = pickle.loads(b"".join(data))

client.close()

while True:
    cv2.imshow("Input",frame)#show in a window
    c= cv2.waitKey(1)#receive a keyboard key typed
    if c == 27:#if the keyboard key is ESC, leave to while (BREAK)
        break

#When to leave while
cv2.destroyAllWindows()# close all windows