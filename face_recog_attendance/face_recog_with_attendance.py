# -*- coding: utf-8 -*-

import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
# from PIL import ImageGrab
 
path = 'image_attendance'
images = []
class_names = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    class_names.append(os.path.splitext(cl)[0])
print(class_names)
 
def find_encodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList
 
def mark_attendance(name):
    with open('Attendance.csv','r+') as f:
        my_data_list = f.readlines()
        name_list = []
        for line in my_data_list:
            entry = line.split(',')
            name_list.append(entry[0])
        if name not in name_list:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')
 
#### FOR CAPTURING SCREEN RATHER THAN WEBCAM
# def captureScreen(bbox=(300,300,690+300,530+300)):
#     capScr = np.array(ImageGrab.grab(bbox))
#     capScr = cv2.cvtColor(capScr, cv2.COLOR_RGB2BGR)
#     return capScr
 
encode_list_known = find_encodings(images)
print('Encoding Complete')
 
cap = cv2.VideoCapture(0)
 
while True:
    success, img = cap.read()
    #img = captureScreen()
    img_small = cv2.resize(img,(0,0),None,0.25,0.25)
    img_small = cv2.cvtColor(img_small, cv2.COLOR_BGR2RGB)
 
    faces_current_frame = face_recognition.face_locations(img_small)
    encodes_current_frame = face_recognition.face_encodings(img_small,faces_current_frame)
 
    for encodeFace,faceLoc in zip(encodes_current_frame,faces_current_frame):
        matches = face_recognition.compare_faces(encode_list_known,encodeFace)
        face_distance = face_recognition.face_distance(encode_list_known,encodeFace)
        #print(faceDis)
        match_index = np.argmin(face_distance)
 
        if matches[match_index]:
            name = class_names[match_index].upper()
            #print(name)
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            mark_attendance(name)
            
        else:
            y1,x2,y2,x1 = faceLoc
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(img,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(img,"UNKNOWN",(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
 
    cv2.imshow('Webcam',img)
    cv2.waitKey(1)