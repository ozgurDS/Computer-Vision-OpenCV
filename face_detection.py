import cv2
import numpy as np

path = "Images/adile nasit.jpg"
img = cv2.imread(path)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Using pretrained OpenCV face cascade

cascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
faces = cascade.detectMultiScale(img_gray, 1.1, 5)

#Creating boundary boxes around detected faces

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255),2)

cv2.imshow("Output", img)


cv2.waitKey(0)
cv2.destroyAllWindows()