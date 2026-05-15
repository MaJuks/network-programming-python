from configparser import Interpolation
import cv2
import socket
import pickle

port = 8084


#open webcam
cap = cv2.VideoCapture(0)

#verify if the webcam has been open
if not cap.isOpened():
    raise IOError("problem to acess the webcam")

#object Socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#associa the socket for a port
server.bind("0.0.0.0",port)
server.listen()

#server keep waiting connection
while True:
    print(f"***Server waiting in the port {port}***")

    #accept the connection
    conn, addr = server.accept()
    print(f"== connection received OF {addr} ==")

    #capture a frame
    ret,frame = cap.read() 
    #change size of frame
    frame = cv2.resize(frame,None, fx=0.5,fy=0.5,interpolation = cv2.INTER_AREA) 
    
    #pack the frame
    dados = pickle.dumps(frame)

    #send the frames's pack
    conn.send(dados)

    #close the connection
    conn.close()
    print("== client disconnected == ")
    