import cv2 as cv
from IPython.display import display, clear_output
from matplotlib import pyplot as plt
# %matploitlib inline

# Import libraries to recocnicer
face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eyes_cascade = cv.CascadeClassifier('./haarcascade_eye.xml')
body_cascade = cv.CascadeClassifier('./haarcascade_fullbody.xml')
# Save image
img = cv.imread('./rostro11.jpg')
# Convert to scale gray
imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
plt.imshow(imgGray,interpolation='bicubic', cmap='gray')


bodyes = body_cascade.detectMultiScale(imgGray, 1.012, 2)
for( bx, by, bw, bh) in bodyes:
    cv.rectangle(img, (bx,by), (bx+bw,by+bh), (255,0,0), 2)


plt.imshow(img)
cv.imshow('Deteccion de rostros', img)
cv.waitKey(0)
cv.destroyAllWindows()

# 6183170878


