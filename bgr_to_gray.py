import cv2
import numpy as np 

img = cv2.imread("Images/butterfly.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Original", img)
cv2.imshow("Gray", img_gray)

#Properties of the original image

height, width, channels = img.shape
print("Original Shape: ", height, width, channels)

#Properties of the gray image (we exclude channel propertie since its gray)

height, width = img_gray.shape
print("Gray Shape: ", height, width)

#Convert image to gray while calling it:
# img = cv2.imread("Images/butterfly.jpg",0)




cv2.waitKey(0)
cv2.destroyAllWindows()