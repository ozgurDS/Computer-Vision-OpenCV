import cv2
import numpy as np

img = cv2.imread("Images/kemal sunal.jpg")

#Green effect to eyes

img[130:190,350:490,1] = 255

cv2.imshow("Kemal Sunal",img)



cv2.waitKey(0)
cv2.destroyAllWindows()