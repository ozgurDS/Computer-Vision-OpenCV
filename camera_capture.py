import cv2
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3,640)    #Changing width to 640
cap.set(4,480)    #Changing height to 480
cap.set(10,100)   #Changing brightness to 100

while True:
    success, frame = cap.read()
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)   ##If we want gray capture 
    cv2.imshow("Capture", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
