# import cv2

# #Loading The Cascade File
# face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# #Reading the Input Image
# #image= cv2.imread('1.jpg')
# image= cv2.imread('1.png')

# #Resizing the Image
# img = cv2.resize(image,None,fx=0.3,fy=0.3)

# #Converting the image into grayscale image
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# #Detecting The Faces
# faces = face_cascade.detectMultiScale(imgGray, 1.2, 5)

# #Pointing The Faces
# for (x,y,w,h) in faces:
# 	cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)

# #Displaying The Output Image
# cv2.imshow('img', img)
# cv2.waitKey()






import cv2
import os
import sys

# Full paths to cascade and image files
cascade_path = "/home/prakhar/python-learning/python_Basic-to-advance/Day_2/3. Face Recognition/haarcascade_frontalface_default.xml"
image_path = "/home/prakhar/python-learning/python_Basic-to-advance/Day_2/3. Face Recognition/1.png"

# Check if cascade file exists
if not os.path.isfile(cascade_path):
    print(f"Error: Cascade file not found at {cascade_path}")
    sys.exit(1)

# Load the cascade classifier
face_cascade = cv2.CascadeClassifier(cascade_path)

# Check if image file exists
if not os.path.isfile(image_path):
    print(f"Error: Image file not found at {image_path}")
    sys.exit(1)

# Read the input image
image = cv2.imread(image_path)

# Resize image for faster processing
img = cv2.resize(image, None, fx=0.3, fy=0.3)

# Convert to grayscale for face detection
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect faces
faces = face_cascade.detectMultiScale(imgGray, scaleFactor=1.2, minNeighbors=5)

# Draw rectangles around faces
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

# Display the output image with detected faces
cv2.imshow('Detected Faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
