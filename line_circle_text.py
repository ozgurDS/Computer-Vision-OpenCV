import cv2
import numpy as np

img = np.zeros((300,300,3), dtype = "uint8")

cv2.line(img,(0,0),(100,100),(0,0,255),2)
cv2.circle(img, (150,150), 20, (0,255,0),2)
cv2.putText(img, "Narsilion", (0,250), cv2.FONT_HERSHEY_COMPLEX, 2, (255,0,0),2)

cv2.imshow("Test",img)

cv2.waitKey(0)
cv2.destroyAllWindows()