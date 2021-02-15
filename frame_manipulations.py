import cv2
import numpy as np

img = cv2.imread("Images/adile nasit.jpg")
cv2.imshow("Adile Nasit",img)

#Mirroring

img_mir = cv2.copyMakeBorder(img,100,100,100,100,cv2.BORDER_REFLECT)
cv2.imshow("Mirrored", img_mir)

#Lengthening

img_l = cv2.copyMakeBorder(img,0,0,0,100,cv2.BORDER_REPLICATE)
cv2.imshow("result", img_l)

#Wrapping

img_wrp = cv2.copyMakeBorder(img,0,0,200,200,cv2.BORDER_WRAP)
cv2.imshow("result", img_wrp)

#Constanting

img_ct = cv2.copyMakeBorder(img,0,0,200,200,cv2.BORDER_CONSTANT, value= (55,55,75))
cv2.imshow("result", img_ct)



cv2.waitKey(0)
cv2.destroyAllWindows()
