from configparser import Interpolation
import cv2

#open webcam
cap = cv2.VideoCapture(0)

#verify if the webcam has been open
if not cap.isOpened():
    raise IOError("problem to acess the webcam")

while True:
    ret,frame = cap.read() #capture a frame
    frame = cv2.resize(frame,None, fx=0.5,fy=0.5,interpolation = cv2.INTER_AREA) #change size of frame

    cv2.imshow("Input",frame)#show in a window

    c= cv2.waitKey(1)#receive a keyboard key typed
    if c == 27:#if the keyboard key is ESC, leave to while (BREAK)
        break
#When to leave while
cap.release() #release the cam
cv2.destroyAllWindows()# close all windows