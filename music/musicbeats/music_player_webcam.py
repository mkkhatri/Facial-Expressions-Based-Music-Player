#Coded by:- Kushal Bhavsra
#From:- Techmicra IT solution

from django.shortcuts import render,redirect
from django.http import HttpResponse
import webbrowser
import requests
from subprocess import run,PIPE
import sys
import time
import cv2
import label_image
import os,random
import subprocess
from views import musicbeats
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# def musicbeats(a,b):
#     if 1==1:
#         c=a+b
#         print("sad")
#         return c
#
# def sad(request):
#     return render(request, 'index2.html')

size = 4
# We load the xml file
classifier = cv2.CascadeClassifier('musicbeats//haarcascade_frontalface_alt.xml')
global text
webcam = cv2.VideoCapture(0)  # Using default WebCam connected to the PC.
now = time.time()###For calculate seconds of video
future = now +10 ####here is second of time which taken by emotion recognition system ,you can change it
while True:
    (rval, im) = webcam.read()
    im = cv2.flip(im, 1, 0)  # Flip to act as a mirror
    # Resize the image to speed up detection
    mini = cv2.resize(im, (int(im.shape[1] / size), int(im.shape[0] / size)))
    # detect MultiScale / faces
    faces = classifier.detectMultiScale(mini)
    # Draw rectangles around each face
    for f in faces:
        (x, y, w, h) = [v * size for v in f]  # Scale the shapesize backup
        sub_face = im[y:y + h, x:x + w]
        FaceFileName = "test.jpg"  # Saving the current image from the webcam for testing.
        cv2.imwrite(FaceFileName, sub_face)
        text = label_image.main(FaceFileName)  # Getting the Result from the label_image file, i.e., Classification Result.
        text = text.title()  # Title Case looks Stunning.
        font = cv2.FONT_HERSHEY_TRIPLEX

        if text == 'Angry':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0, 25, 255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0, 25,255), 2)

        if text == 'Happy':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,260,0), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0,260,0), 2)

        if text == 'Surprise':
            cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 55), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (255, 0, 55), 2)

        if text == 'Sad':
            cv2.rectangle(im, (x, y), (x + w, y + h), (0,191,255), 7)
            cv2.putText(im, text, (x + h, y), font, 1, (0,191,255), 2)

    # Show the image/
    cv2.imshow('Music player with Emotion recognition', im)
    key = cv2.waitKey(10)
    #if time.time() > future:##after 20second music will play
    if key == 13:
        try:
            cv2.destroyAllWindows()
           # mp = 'C:/Program Files (x86)/Windows Media Player/wmplayer.exe'




            if text == 'Angry':
            # randomfile = random.choice(os.listdir("C:/Music_player_with_Emotions_recognition-master/songs/Sad/"))
            # print('You are sad,dont worry:) ,I am playing song for you: ' + randomfile)
            # file = ('C:/Music_player_with_Emotions_recognition-master/songs/Sad/' + randomfile)
            # subprocess.call([mp, file])
                 #url = 'C://djmusic//music//templates//index1.html'

                cv2.rectangle(im,(0,400), (640,455), (0, 255, 0),cv2.FILLED)
                cv2.putText(im,text+" Detected",(200,440),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,255),2)
                cv2.imshow("Detect your emotions here", im)
                cv2.waitKey(1000)
                url = 'E://Facial Expressions Based Music Player//music//templates//Angry//default.html'
                webbrowser.open(url, new=1)
                break
            
            if text == 'Happy':
            # randomfile = random.choice(os.listdir("C:/Music_player_with_Emotions_recognition-master/songs/Sad/"))
            # print('You are sad,dont worry:) ,I am playing song for you: ' + randomfile)
            # file = ('C:/Music_player_with_Emotions_recognition-master/songs/Sad/' + randomfile)
            # subprocess.call([mp, file])
                 #url = 'C://djmusic//music//templates//index1.html'

                cv2.rectangle(im,(0,400), (640,455), (0, 255, 0),cv2.FILLED)
                cv2.putText(im,text+" Detected",(200,440),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,255),2)
                cv2.imshow("Detect your emotions here", im)
                cv2.waitKey(1000)
                url = 'E://Facial Expressions Based Music Player//music//templates//Happy//default.html'
                webbrowser.open(url, new=1)
                break
            
            if text == 'Sad':
            # randomfile = random.choice(os.listdir("C:/Music_player_with_Emotions_recognition-master/songs/Sad/"))
            # print('You are sad,dont worry:) ,I am playing song for you: ' + randomfile)
            # file = ('C:/Music_player_with_Emotions_recognition-master/songs/Sad/' + randomfile)
            # subprocess.call([mp, file])
                 #url = 'C://djmusic//music//templates//index1.html'

                cv2.rectangle(im,(0,400), (640,455), (0, 255, 0),cv2.FILLED)
                cv2.putText(im,text+" Detected",(200,440),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,255),2)
                cv2.imshow("Detect your emotions here", im)
                cv2.waitKey(1000)
                url = 'E://Facial Expressions Based Music Player//music//templates//Sad//default.html'
                webbrowser.open(url, new=1)
                break

            if text == 'Surprise':
            # randomfile = random.choice(os.listdir("C:/Music_player_with_Emotions_recognition-master/songs/Sad/"))
            # print('You are sad,dont worry:) ,I am playing song for you: ' + randomfile)
            # file = ('C:/Music_player_with_Emotions_recognition-master/songs/Sad/' + randomfile)
            # subprocess.call([mp, file])
                 #url = 'C://djmusic//music//templates//index1.html'

                cv2.rectangle(im,(0,400), (640,455), (0, 255, 0),cv2.FILLED)
                cv2.putText(im,text+" Detected",(200,440),cv2.FONT_HERSHEY_TRIPLEX,1,(0,0,255),2)
                cv2.imshow("Detect your emotions here", im)
                cv2.waitKey(1000)
                url = 'E://Facial Expressions Based Music Player//music//templates//Surprise//default.html'
                webbrowser.open(url, new=1)
                break    
        except:
            print('Please stay focus in Camera frame atleast 15 seconds & run again this program:)')
            break

    if key == 27:  # The Esc key
        break
