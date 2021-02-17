import cv2
import numpy as np 

def getContours(img_in):
    contours, hierarcy = cv2.findContours(img_in, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area >10: #Adding a logical threshold prevents detection of some small unnecessary areas
         cv2.drawContours(img_contour, cnt, -1, (255,255,255),2)
         par = cv2.arcLength(cnt, True)
         approx = cv2.approxPolyDP(cnt, 0.02*par, True) #The corner points for each contour
         print(len(approx)) #This gives us the number of corner points for each contour
         
         corner = len(approx)
         x,y,w,h = cv2.boundingRect(approx) 

         if corner ==3: obj_type = "Triangle"
         elif corner ==4:
             asp_ratio = w/float(h) #Since we dealing with decimal numbers, we need to make 1 of them float
             if asp_ratio > 0.95 and asp_ratio < 1.05: obj_type ="Square"
             else: obj_type = "Rectangle"
         elif corner ==5: obj_type = "Pentagon"
         elif corner ==6: obj_type = "Hexagon"
         elif corner >6: obj_type = "Circle"
         else: obj_type="None"

         cv2.rectangle(img_contour,(x,y),(x+w, y+h), (0,255,0), 2)
         cv2.putText(img_contour,obj_type, (x+(w//2)-20,y+(h//2)), 
         cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,255,255), 1)


path = "Images/shapes.png"
img = cv2.imread(path)

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (5,5), 1)
img_canny = cv2.Canny(img_blur,50,50)
img_blank = np.zeros_like(img_gray)
img_contour = img.copy()
getContours(img_canny)

cv2.imshow("Original", img)
cv2.imshow("Contours", img_contour)
cv2.imshow("Stack",np.hstack([img_gray, img_blur, img_canny, img_blank]))



cv2.waitKey(0)
cv2.destroyAllWindows()