import cv2
import numpy as np 

img = cv2.imread("Images/bw.jpg")
kernel = np.ones((5,5),np.uint8)
cv2.imshow("original",img)

#-------Erosion------

erosion = cv2.erode(img, kernel, iterations=1)
erosion2 = cv2.erode(img, kernel, iterations=2)

cv2.imshow("erotion1",erosion)
#cv2.imshow("erotion2",erosion2)

#-------Dilation-------

dilation = cv2.dilate(img, kernel, iterations=1)
dilation2 = cv2.dilate(img, kernel, iterations=2)

cv2.imshow("dilation1",dilation)
#cv2.imshow("dilation2",dilation2)

#------First erosion then dilation------

combined = cv2.dilate(erosion, kernel, iterations=1)
cv2.imshow("Combined", combined)

#-----Doing first erosion then dilation using Opening-----

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN,kernel)
cv2.imshow("Opening", opening)

#-----Doing first dilation then erosion using Closing-----

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
cv2.imshow("Closing", closing)

#---Gradient (Diolation minus Erosion)

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
cv2.imshow("Gradient", gradient)

#----Tophat  (img minus Opening)----

tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
cv2.imshow("Tophat", tophat)

#----Blackhat (img minus CLosing)----

blackhat= cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
cv2.imshow("Blackhat", blackhat)



cv2.waitKey(0)
cv2.destroyAllWindows()
