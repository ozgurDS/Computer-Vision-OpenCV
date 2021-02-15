import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    
    ret, frame = cap.read()

    cv2.rectangle(frame,(100,100),(200,200),(0,0,255),2)
    cv2.line(frame, (30,100), (100,100), (0,255,0),2)
    cv2.circle(frame, (300,300), 30, (255,0,0), 1)
    cv2.putText(frame, "Narsilion", (0,400), cv2.FONT_HERSHEY_DUPLEX,2, (255,255,255), 2)

    cv2.imshow("Capture", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()