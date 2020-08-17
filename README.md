
# REAL TIME FACE RECOGNITION WITH ATTENDANCE SYSTEM.
# INTRODUCTION

Attendance maintenance is a significant function in all the institutions to monitor the performance of the students. Every institute does this in its own way. Some of these institutes use the old paper or file based systems and some have adopted strategies of automatic attendance using some biometric techniques.  A facial recognition system is a computerized biometric software which is suited for determining or validating a person by performing comparison on patterns based on their facial appearances. Face recognition systems have upgraded appreciably in their management over the recent years and this technology is now vastly used for various objectives like security and in commercial operations. Face recognition is a powerful field of research which is a computer based digital technology. Face recognition for the intent of marking attendance is a resourceful application of attendance system. It is widely used in security systems and it can be compared with other biometrics such as fingerprint or eye iris recognition systems. As the number of students in an educational institute or employees at an organization increases, the needs for lecturers or to the organization also increase the complication of attendance control. This project may be helpful for the explanation of these types of problems. The number of students present in a lecture hall is observed, each person is identified and then the information about the number of students who are present.


# OVERVIEW

Face recognition being a biometric technique implies determination if the image of the face of any particular person matches any of the face images that are stored in a database. This difficulty is tough to resolve automatically because of the changes that several factors, like facial expression, aging and even lighting can affect the image. Facial recognition among the various biometric techniques may not be the most authentic but it has various advantages over the others. Face recognition is natural, feasible and does not require assistance. The expected system engages the face recognition approach for the automating the attendance procedure of students or employees without their involvement. A web cam is used for capturing the images of students or employees. The faces in the captured images are detected and compared with the images in database and the attendance is marked.

## IMAGE PROCESSING

The facial recognition process can be split into two major stages: processing which occurs before detection involving face detection and alignment and later recognition is done using feature extraction and matching steps.
	

 1. FACE DETECTION
		 The primary function of this step is to conclude whether the human faces emerge in a given image, and what is the location of these faces. The expected outputs of this step are patches which contain each face in the input image. In order to get a more robust and easily designable face recognition system.
		 
 2. FEATURE EXTRACTION
		 Following the face detection step the extraction of human face patches from images is done. After this step, the conversion of face patch is done into vector with fixed coordinates or a set of landmark points.
		 
 3. FACE RECOGNITION
		The last step after the representation of faces is to identify them. For automatic recognition we need to build a face database. Various images are taken foe each person and their features are extracted and stored . Then when an input image is fed the face detection and feature extraction is performed and its feature to each face class is compared and stored.
		
 4. MARKING ATTENDANCE
		 After detecting the faces the attendance of the student is marked and the entry of the student is made in a csv file and saved the attendance is marked only once.

## DEMO

![alt-text](https://github.com/akhiilkasare/face-recognition-with-attendance-system/blob/master/face_recog_attendance/face_recognition.gif)

