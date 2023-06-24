# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 20:03:04 2023

@author: Nagihan
"""

import cv2
import numpy as np

cap = cv2.VideoCapture("traffic2.mp4")

#video boyutlarını al
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#yeniden boyutlandır
new_width = 640
new_height = 480

#codec
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter('new_traffic.mp4',fourcc,30.0,(new_width, new_height))

#arka planı temizlemek için nesneleri öne çıkarmak için maske
backsub = cv2.createBackgroundSubtractorMOG2()

count = 0

while True:
    
    ret,frame = cap.read()
    
    
    if ret:
        
        resized_frame = cv2.resize(frame, (new_width, new_height))
        
        fgmask = backsub.apply(resized_frame)
        
    #    cv2.line(resized_frame, (0,70),(510,70),(0,255,0),2)
    #    cv2.line(resized_frame, (0,120),(510,120),(0,255,0),2)
    
        cv2.line(resized_frame, (0,300),(540,300),(0,255,0),2)
        cv2.line(resized_frame, (0,340),(540,340),(0,255,0),2)
        
        contours, hiers = cv2.findContours(fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        
        try: hiers = hiers[0]
        except: hiers = []
        
        for contour, hier in zip(contours,hiers):
            (x,y,w,h) = cv2.boundingRect(contour)
            
            if w>40 and h>40:
                cv2.rectangle(resized_frame,(x,y),(x+w,y+h),(255,0,0),3)
                if y>300 and y>340:
                    count+=1
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(resized_frame,"car "+str(count),(90,100),font,2, cv2.LINE_AA)
        
        
    
    
    
        cv2.imshow("cap",fgmask)
        cv2.imshow("cap2", resized_frame)
        if cv2.waitKey(40) & 0xFF == ord("q"):
            break
        
    

cap.release()
cv2.destroyAllWindows()