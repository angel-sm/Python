import cv2 as cv
from IPython.display import display, clear_output
from matplotlib import pyplot as plt
# %matploitlib inline

# Import libraries to recocnicer
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv.CascadeClassifier('./haarcascade_eye.xml')
body_cascade = cv.CascadeClassifier('./haarcascade_fullbody.xml')
# Save image
img = cv.imread('./rostro5.jpg')
# Convert to scale gray
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(imgGray,interpolation='bicubic', cmap='gray')

# # Save coordenades
faces = face_cascade.detectMultiScale(imgGray, 1.3, 5)

# draw rectangle in coordenades of face detected
for ( x, y, w, h ) in faces:
        # Draw rectangle
        cv.rectangle(img,(x,y), (x+w, y+h), (0,255,0), 2)
        # roi : Region de interes
        roi_gray = imgGray[y:y+h, x:x+w]
        roi_color = img[y:y+w, x:x+w]

        eyes = eyes_cascade.detectMultiScale(roi_gray)
        for( ex, ey, ew, eh) in eyes:
            cv.rectangle(roi_color, (ex,ey), (ex+ew,ey+eh), (0,0,255), 2)


plt.imshow(img)
cv.imshow('Deteccion de rostros', img)
cv.waitKey(0)
cv.destroyAllWindows()



