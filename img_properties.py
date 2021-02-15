import cv2
import numpy as np 

img = cv2.imread("Images/wolf.jpg")
cv2.imshow("wolf",img)

print("Size: "+str(img.size))
print("Shape: "+str(img.shape))
print("Data type: "+str(img.dtype))

#Resizing the image

img_resize = cv2.resize(img,(300,200)) #Adjusting new image width to 300 and height to 200
cv2.imshow("Resized",img_resize)



cv2.waitKey(0)
cv2.destroyAllWindows()

