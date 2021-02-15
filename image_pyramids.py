import cv2
import numpy as np 

img = cv2.imread("Images/car1.jpg")
img_doublesize = cv2.pyrUp(img)
img_halfsize = cv2.pyrDown(img)

cv2.imshow("Org",img)
cv2.imshow("Double Size",img_doublesize)
cv2.imshow("Half Size",img_halfsize)

print("Org Img Shape",img.shape)
print("Double Size Img Shape",img_doublesize.shape)
print("Half Size Img Shape",img_halfsize.shape)

#Making our own img full of zeros

img_zeros = np.zeros((300,300,3), dtype = "uint8")
print(img_zeros)



cv2.waitKey(0)
cv2.destroyAllWindows()