import cv2
import numpy as np 

img = cv2.imread("Images/noised3.png")
cv2.imshow("Original",img)

#Mean Filter

img_mean1 = cv2.blur(img, (3,3))
img_mean2 = cv2.blur(img, (5,5))

cv2.imshow("Mean Filtered 1", img_mean1)
cv2.imshow("Mean Filtered 2", img_mean2)

#Median Filter

img_median1 = cv2.medianBlur(img, 3)
img_median2 = cv2.medianBlur(img, 5)

cv2.imshow("Median Filtered 1", img_median1)
cv2.imshow("Median Filtered 2", img_median2)

#Gaussian Fİlter

img_gauss1 = cv2.GaussianBlur(img, (3,3), 0)
img_gauss2 = cv2.GaussianBlur(img, (5,5), 0)

cv2.imshow("Gaussian Filtered 1", img_gauss1)
cv2.imshow("Gaussian Filtered 2", img_gauss2)



cv2.waitKey(0)
cv2.destroyAllWindows()
