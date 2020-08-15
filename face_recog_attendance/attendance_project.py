

import cv2
import numpy as np
import face_recognition
from datetime import datetime
import os

path = 'image_attendance'

images = []
class_name = []
# Grabbing the list of images from the folder
myList = os.listdir(path)
print(myList)

''' Step 1 : Listing all the images from the folder 1 by 1 '''
for cls in myList:
    curr_image = cv2.imread(f'{path}/{cls}')
    images.append(curr_image)
    class_name.append(os.path.splitext(cls)[0])
print(class_name)

'''Ones we load the images we need to find the encoding for each one of them'''

''' Step 2 : Creating a function which will compute all the encodings for us '''

def find_encodings(images):
    encoded_list = []
    # Looping through all the images 
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode  = face_recognition.face_encodings(img)[0]
        encoded_list.append(encode)
    return encoded_list

# Marking the attendance
def mark_attendance(name):
    with open('Attendance.csv', 'r+') as f:
        # If somebody arrives we dont want to repeat it
        my_data_list = f.readline()
        name_list = []
        for line in my_data_list:
            entry = line.split(',')
            name_list.append(entry[0])
        
        if name not in name_list:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')
        

encode_known_list = find_encodings(images)
print('Encoding Complete')

''' Step 3 : To find the matches in our encodings '''

# Initializing the web cam 
cap = cv2.VideoCapture(0)

# Writing a while loop to get each frame
while True:
    success, img = cap.read()
    # As we are doing this in real time we need to reduce the size of the image this will help us in speeding the process
    image_small = cv2.resize(img, (0,0), None, 0.25,0.25)
    # Converting our resized image into RGB
    image_small = cv2.cvtColor(image_small, cv2.COLOR_BGR2RGB)
    # Finding the face locations from the webcam
    faces_current_frame = face_recognition.face_locations(image_small)
    # Finding the encoding of our webcam
    encode_current_frame = face_recognition.face_encodings(image_small, faces_current_frame)
    # Finding the matches in the frame
    for encode_face, face_loc in zip(encode_current_frame, faces_current_frame):
        matches = face_recognition.compare_faces(encode_known_list, encode_face)
        
        face_distance =  face_recognition.face_distance(encode_known_list, encode_face)
        #print(face_distance)
        match_index = np.argmin(face_distance)
        
        if matches[match_index]:
            name = class_name[match_index].upper()
            #print(name)
            # Drawing a rectangle around the face
            y1,x2,y2,x1 = face_loc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img,name, (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            
        else:
            y1,x2,y2,x1 = face_loc
            y1,x2,y2,x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
            cv2.rectangle(img, (x1,y2-35), (x2,y2), (0,255,0), cv2.FILLED)
            cv2.putText(img,"Unknown", (x1+6,y2-6), cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
    mark_attendance(name)
            
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()    
cv2.destroyAllWindows()
        
    
    
    





    















#img_elon = face_recognition.load_image_file('images/elon_musk.jpg')
#img_elon = cv2.cvtColor(img_elon, cv2.COLOR_BGR2RGB)

#img_elon_test = face_recognition.load_image_file('images/elon_test.jpeg')
#img_elon_test = cv2.cvtColor(img_elon_test, cv2.COLOR_BGR2RGB)

