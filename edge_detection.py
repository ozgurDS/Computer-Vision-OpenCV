import cv2
import numpy as np 

img = cv2.imread("Images/wolf.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray,(3,3),0)

#------Using Canny------

wide = cv2.Canny(img_blur, 10,200)
tight = cv2.Canny(img_blur, 150,200)

#------Defining an autoCanny function-------

def autoCanny(img_blur, sigma=0.8):
    median = np.median(img_blur)
    lower = int(max(0,(1.0-sigma)*median))
    upper = int(min(255,(1.0)+sigma)*median)
    img_canny = cv2.Canny(img_blur,lower, upper)

    return img_canny

auto = autoCanny(img_blur)

cv2.imshow("Blurred", img_blur)
cv2.imshow("Edges", np.hstack([wide, tight, auto]))



cv2.waitKey(0)
cv2.destroyAllWindows()