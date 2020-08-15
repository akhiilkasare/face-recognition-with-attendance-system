#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:10:34 2020

@author: akhil
"""

import cv2
import numpy as np
import face_recognition

# Step 1 :  Loading the images and converting them into RGB's


img_elon = face_recognition.load_image_file('images/elon_musk.jpg')
# we get the image in BGR and library understands it into RGB's. Converting the image into RGB
img_elon = cv2.cvtColor(img_elon, cv2.COLOR_BGR2RGB)


# Doing the same with 
test_img_elon = face_recognition.load_image_file('images/elon_test.jpeg')
# we get the image in BGR and library understands it into RGB's. Converting the image into RGB
test_img_elon = cv2.cvtColor(test_img_elon, cv2.COLOR_BGR2RGB)
#-------------------------------------------------------------------------------------------------------------------

# Step2 : Finding the faces in the images and finding their encodings as well

face_loc = face_recognition.face_locations(img_elon)[0]
encode_elon = face_recognition.face_encodings(img_elon)[0]
cv2.rectangle(img_elon, (face_loc[3], face_loc[0]), (face_loc[1], face_loc[2]), (255,255,0), 2)

# Doing the same with our test image

face_loc_test = face_recognition.face_locations(test_img_elon)[0]
encode_test_elon = face_recognition.face_encodings(test_img_elon)[0]
cv2.rectangle(test_img_elon, (face_loc_test[3], face_loc_test[0]), (face_loc[1], face_loc_test[2]), (255,255,0), 2)

# ------------------------------------------------------------------------------------------------------------------

# Step 3 : Comparing these faces and finding the distance between them using linear SVM at the back end to finf whether they match or not
    
results = face_recognition.compare_faces([encode_elon], encode_test_elon)
# IF it returns true it means that encoings match if false then encodings dont match
face_dis = face_recognition.face_distance([encode_elon], encode_test_elon)
print(results, face_dis)

cv2.putText(img_elon, f'{results} {round(face_dis[0],2)}', (50,50), cv2.FONT_HERSHEY_COMPLEX,1, (255,255,0),2)


cv2.imshow('Elon Musk', img_elon)
cv2.imshow('Elon Musk Test', test_img_elon)


cv2.waitKey(0)

cv2.destroyAllWindows()