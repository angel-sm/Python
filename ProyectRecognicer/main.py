#Ejemplo de deteccion facial con OpenCV y Python
#Por Glare
#www.robologs.net
 
import numpy as np
import cv2
 
#cargamos la plantilla e inicializamos la webcam:
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

img_counter = 0

while(True):
    #leemos un frame y lo guardamos
    ret, img = cap.read()
    k = cv2.waitKey(1)
 
    #convertimos la imagen a blanco y negro
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    #buscamos las coordenadas de los rostros (si los hay) y
    #guardamos su posicion
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
 
    #Dibujamos un rectangulo en las coordenadas de cada rostro
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(125,255,0),2)
        roi_color = img[y:y+w, x:x+w]

    # Mostramos la imagenq
    cv2.imshow('img',img)

    if k%256 == 32:
        # SPACE pressed
        img_name = "./img/picture{}.png".format(img_counter)
        # cv2.imwrite(img_name, img)
        cv2.imwrite(img_name, roi_color)
        print("{} written!".format(img_name))
        img_counter += 1
             
    # con la tecla 'q' salimos del programa
    if k & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()