import cv2
import numpy as np

img = cv2.imread("Images/23 nisan.jpg")
cv2.imshow("23 Nisan",img)

#Sectioning

section = img[50:150,300:400]
cv2.imshow("Section",section)

#Adding section to the image

img[0:100,0:100] = section

cv2.imshow("New", img)


cv2.waitKey(0)
cv2.destroyAllWindows()