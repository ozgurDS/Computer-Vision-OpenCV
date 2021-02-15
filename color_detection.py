import cv2
import numpy as np 

path  = "Images/lambo.png"

"""Creating track bars to play around the HSV values real time 
to determine the HSV values of the red color of the car"""

def empty():
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)

#Creating trackbars and threshold values (already adjusted after using the mask)

cv2.createTrackbar("Hue Min", "TrackBars", 0, 179, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 15, 179, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 35, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 95, 255, empty)
cv2.createTrackbar("Val Max", "TrackBars", 255, 255, empty)

#Reading trackbar values

while True:

    img = cv2.imread(path)
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("Val Max", "TrackBars")
    print(h_min,h_max,s_min,s_max,v_min,v_max)

    #Creating a mask to determine the HSV values of the red color of the car

    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])
    img_mask = cv2.inRange(img_hsv, lower, upper)

    #Getting the red color of the car using bitwise and operator
    img_result = cv2.bitwise_and(img,img, mask= img_mask)

    cv2.imshow("Original", img)
    cv2.imshow("HSV", img_hsv)
    cv2.imshow("Mask", img_mask)
    cv2.imshow("Result", img_result)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()