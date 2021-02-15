import cv2
import numpy as np

img1 = cv2.imread("Images/emel.jpg")
img2 = cv2.imread("Images/turkan.jpg")

cv2.imshow("Emel Sayin",img1)
cv2.imshow("Turkan Soray",img2)


#Weighted Sum

print(img1[0,980])
print(img2[200,300])
print(img1[0,980] + img2[200,300])

#Image Addition (images must be same size)

img3 = cv2.imread("Images/car1.jpg")
img4 = cv2.imread("Images/car2.jpg")

img_add = cv2.addWeighted(img3, 0.7, img4, 0.3, 0)

cv2.imshow("Summed Images", img_add)




cv2.waitKey(0)
cv2.destroyAllWindows()