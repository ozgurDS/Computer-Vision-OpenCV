import cv2
import numpy as np

img = cv2.imread("Images/hababam.jpg")

print(img[50,50])

#Rectangling

cv2.rectangle(img, (250,200),(320,120), [0,0,255],2)
cv2.imshow("Hababam",img)






cv2.waitKey(0)
cv2.destroyAllWindows()