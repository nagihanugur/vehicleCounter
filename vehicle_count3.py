# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 21:59:50 2023

@author: Nagihan
"""

import cv2
import numpy as np

cap = cv2.VideoCapture("video.avi")
backsub = cv2.createBackgroundSubtractorMOG2()


count = 0


    
while True:
        
    ret, frame = cap.read()
        
    if ret:
            
        fgmask = backsub.apply(frame)
        
        cv2.line(frame, (50,0), (50,300), (0,255,0), 2)
        cv2.line(frame, (70,0), (70,300), (0,255,0), 2)
            
        contours, hiers = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        try: hiers = hiers[0]
        except: hiers = []
            
        for contour, hier in zip(contours, hiers):
            (x,y,w,h) = cv2.boundingRect(contour)
            if w > 40 and h > 40:
                cv2.rectangle(frame, (x,y),(x+w, y+h), (255,0,0), 2)
                if x > 50 and x < 70:
                    count+=1
               
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, "Car: "+str(count), (90, 100), font, 2, (0,0,255), 2, cv2.LINE_AA)
            
        cv2.imshow("Takip", frame)
        cv2.imshow("Arka plan çıkar",fgmask)
            
        key = cv2.waitKey(40)
        if key == ord('q'):
            break
                  
        
capture.release()
cv2.destroyAllWindows()
                        