from os import system

system('color a')
print('loading...')

import cv2
from random import randint
from time import time
cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier('C:\\Users\\Student\\Documents\\very_important\\haarcascade_frontalface_default.xml')
start = time() 
while time() - start < 30:
    tr, img = cap.read()

    if not tr:
        break
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("yo!", img_gray)
    cv2.imshow("you're lasy!", img)
    #try:
    faces = face_cascade.detectMultiScale(img_gray)
    
    for x, y, width, height in faces:
        
        cv2.putText(img, 'BEZDELNIK!', (x+10,y-10), cv2.FONT_HERSHEY_PLAIN, int(width/70), (randint(0,255),randint(0,255),randint(0,255)), 4)
        cv2.rectangle(img, (x,y), (x+width, y+height), (randint(0,255),randint(0,255),randint(0,255)), 4)
    #except:
    #    pass
    cv2.imshow("you're lasy!", img)
    key = cv2.waitKey(1)

    if key == 27:
        break
    
cv2.destroyAllWindows()
cap.release()
