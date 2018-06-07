#-*-encoding=utf-8-*-

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
min_color = np.array([150,150,50])
max_color = np.array([180,255,150])

while True:
    value , frame = cap.read()
    hsv_frame = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame , min_color , max_color )
    out = cv2.bitwise_and(frame , frame , mask= mask)
    
    #blur&smoot filtreleri
    kernel = np.ones((15,15),np.float32)/225
    smooted = cv2.filter2D(out,-1,kernel)
    blur = cv2.GaussianBlur(out,(15,15),0)
    median = cv2.medianBlur(out , 15)
    bilateral = cv2.bilateralFilter(out,15,75,75)
    
    cv2.imshow("frame",frame)
    cv2.imshow("out",out)
    
    if cv2.waitKey(5) & 0xff == ord("q"):
        cap.release()
        cv2.destroyAllWindows()
        break