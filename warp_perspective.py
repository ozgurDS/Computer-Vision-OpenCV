import cv2
import numpy as np 

img = cv2.imread("Images/cards.png")
cv2.imshow("Image", img)

width,height = 250,350  #Ratio of a card

pts1 = np.float32([[490,64], [619,80], [507,207], [670,226]])  #Corner points of the "Red Wolf" Ace
pts2 = np.float32([[0,0], [width, 0], [0, height], [width,height]]) #Defining which koordinate will be which point
matrix = cv2.getPerspectiveTransform(pts1,pts2) #Defining the transformation matrix

img_out = cv2.warpPerspective(img, matrix, (width,height)) #Warping perspective to bird eye
cv2.imshow("Output", img_out)


cv2.waitKey(0)
cv2.destroyAllWindows()