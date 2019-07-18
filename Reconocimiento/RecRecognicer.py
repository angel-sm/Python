import cv2 as cv
import numpy as np 
cam = cv.VideoCapture(0)

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')


k=4
while(True):
    ret,frame = cam.read()
    print(frame)
    cv.imshow('Presione la tecla ESC para salir', frame)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break