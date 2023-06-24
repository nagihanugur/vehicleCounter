# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 21:25:28 2023

@author: Nagihan
"""

#aracsayma2

import cv2
import numpy as np

cap = cv2.VideoCapture("traffic2.mp4")

car_cascade = cv2.CascadeClassifier('car.xml')

#video boyutlarını al
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#yeniden boyutlandır
new_width = 640
new_height = 480


#arac sayısını tut

count = 0

while True:
    
    #görüntüyü kare kare oku
    ret,frame = cap.read()
    
    
    if ret:
        
        resized_frame = cv2.resize(frame, (new_width, new_height))
        
       
        cv2.line(resized_frame, (0,300),(540,300),(0,255,0),2)
        cv2.line(resized_frame, (0,350),(540,350),(0,255,0),2)
        
        gray = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2GRAY)
       
        cars = car_cascade.detectMultiScale(gray, 1.3,3)
        
    
        
        for x,y,w,h in cars:
            
            cv2.rectangle(resized_frame, (x,y),(x+w, y+h),(0,0,255),2)
            count +=1
            
            
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(resized_frame,"car "+str(count),(90,100),font,2,(0,255,0),2,cv2.LINE_AA)
            
        
        cv2.imshow("cap2", resized_frame)
        if cv2.waitKey(40) & 0xFF == ord("q"):
            break
        
    

cap.release()
cv2.destroyAllWindows()