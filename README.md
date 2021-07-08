# Facial-Expressions-Based-Music-Player
#
The basic work is to identify the expression on the human face that is captured by the webcam. whatever the emotion detected in the webcam according to that one can be directed to the respective emotion song page like a happy, sad, angry, surprise.
#
Now the question is how these all emotions are detected…? Using machine learning’s library OpenCV and TensorFlow framework and haar-cascade classifier we are able to detect the expression. 
#
OpenCV already contains the pre-trained classifiers for a face like lips, eye, nose,etc.. we have trained around 5000 images for better emotion recognization.
#
1.	Facial Detection — Ability to detect the location of face in any input image or frame. The output is the bounding box coordinates of the detected faces
2.	Emotion Detection — Classifying the emotion on the face as happy, angry, sad, neutral, surprise, disgust or fear
#
Database: IndexDb
1.	It will store data inside a user's browser. Because it lets you create web applications with rich query abilities regardless of network availability.
2.	your applications can work both online and offline.
3.	IndexedDB is a low-level API for client-side storage of significant amounts of structured data, including files/blobs. 
4.	This API uses indexes to enable high-performance searches of this data. it is less useful for storing larger amounts of structured data.
