import cv2
import numpy as np 

img = cv2.imread("Images/wolf.jpg",0)
cv2.imshow("Original", img)

#------Simple Thresholdings------

ret, th1 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img, 125, 255, cv2.THRESH_BINARY_INV)
ret, th3 = cv2.threshold(img, 125, 255, cv2.THRESH_TRUNC)
ret, th4 = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO)
ret, th5 = cv2.threshold(img, 125, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow("Thresh 1", th1)
cv2.imshow("Thresh 2", th2)
cv2.imshow("Thresh 4", th4)
cv2.imshow("Thresh 3", th3)
cv2.imshow("Thresh 5", th5)

#-----Adaptive Thresholdings-----

adaptive_th1 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
adaptive_th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("Adaptive 1", adaptive_th1)
cv2.imshow("Adaptive 2", adaptive_th2)

# -----Otsu Threshholding-----

ret, otsu_th = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow("Otsu", otsu_th)




cv2.waitKey(0)
cv2.destroyAllWindows()
